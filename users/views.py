from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone 
from event.models import Enrollment, EventBond as Bond
from datetime import datetime
from .models import UserProfile as PersonalData
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile


def register(request):
    if request.session.get('user_id'):
        return redirect('users:profile')

    if request.method != 'POST':
        return render(request, 'users/register.html')
    
    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password_confirm = request.POST.get('password_confirm')

    if not username or not first_name or not last_name or not email or not password or not password_confirm:
        messages.error(request, 'Todos os campos devem ser preenchidos!')
        return render(request, 'users/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido!')
        return render(request, 'users/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já cadastrado!')
        return render(request, 'users/register.html')

    if password != password_confirm:
        messages.error(request, 'As senhas informadas são diferentes!')
        return render(request, 'users/register.html')

    if len(password) < 8:
        messages.error(request, 'As senhas devem conter mais que 8 caracteres!')
        return render(request, 'users/register.html')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'Username já cadastrado!')
        return render(request, 'users/register.html')

    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    user.save()

    messages.success(request, 'Usuario cadastrado com sucesso!')

    user = auth.authenticate(request, email=email, password=password)
    
    if not user:
        return render(request, 'users/register.html')
    else:
        auth.login(request, user)
        request.session['user_id'] = user.id
        return redirect('users:edit_user', user_id=user.id)

def login(request):
    if request.session.get('user_id'):
        return redirect('users:profile')

    if request.method != 'POST':
        return render(request, 'users/login.html')
    
    email_or_username = request.POST.get('email', '').strip()
    password = request.POST.get('password', '').strip()

    errors = []
    
    if not email_or_username:
        errors.append('O campo email/usuário é obrigatório.')
    
    if not password:
        errors.append('O campo senha é obrigatório.')
    
    if errors:
        for error in errors:
            messages.error(request, error)
        return render(request, 'users/login.html')

    try:
        if '@' in email_or_username:
            user = auth.authenticate(request, email=email_or_username, password=password)
        else:
            user = auth.authenticate(request, username=email_or_username, password=password)

        if not user:
            messages.error(request, 'Credenciais inválidas. Verifique seu email/usuário e senha.')
            return render(request, 'users/login.html')
        
        auth.login(request, user)
        request.session['user_id'] = user.id
        return redirect('users:profile')
            
    except Exception as e:
        messages.error(request, 'Erro no sistema. Tente novamente.')
        return render(request, 'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('users:login')

@login_required(login_url='users:login')
def profile(request):
    try:
        user = request.user
        
        if not user.is_authenticated:
            messages.error(request, 'Usuário não autenticado.')
            return redirect('users:login')
            
        enrollments = Enrollment.objects.filter(user=user)

        return render(request, 'users/profile.html', {
            'user': user, 
            'enrollments': enrollments,
        })
        
    except User.DoesNotExist:
        messages.error(request, 'Sessão expirada. Faça login novamente.')
        return redirect('users:login')
    except Exception as e:
        print(f"Erro no profile: {e}")
        messages.error(request, 'Erro ao carregar perfil.')
        return redirect('users:login')

@login_required(login_url='users:login')
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.session.get('user_id') != user_id:
        return redirect('users:profile')

    if request.method != 'POST':
        bond = Bond.objects.all()
        return render(request, 'users/edit_user.html', {'user': user, 'bond': bond})

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        
        if not hasattr(user, 'personaldata') or user.personaldata is None:
            personal_data = PersonalData()
            personal_data.user = user
            personal_data.save()
        
        user.personaldata.social_network = request.POST.get('social_network')
        user.personaldata.date_of_birth = datetime.strptime(request.POST.get('date_of_birth'), '%d/%m/%Y').date()

        bond_choice_id = request.POST.get('bond_choice')
        user.personaldata.bond_choice = get_object_or_404(Bond, id=bond_choice_id) 

        user.personaldata.rg = request.POST.get('rg')
        
        user.personaldata.save()

        user.save()
        return redirect('users:profile')

@login_required(login_url='users:login')
@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        uploaded_image = request.FILES.get('image')

        if user_id and uploaded_image:
            user = User.objects.get(id=user_id)

            if not hasattr(user, 'personaldata') or user.personaldata is None:
                personal_data = PersonalData()
                personal_data.user = user
                personal_data.save()

            user_profile = user.personaldata

            img = PILImage.open(uploaded_image)

            width, height = img.size
            size = min(width, height)
            left = (width - size) / 2
            top = (height - size) / 2
            right = (width + size) / 2
            bottom = (height + size) / 2

            img = img.crop((left, top, right, bottom))

            img = img.resize((200, 200), PILImage.Resampling.LANCZOS)

            uploaded_image_name = f"profile_picture_{user.username}_{timezone.now().strftime('%Y%m%d%H%M%S')}.jpg"

            buffer = BytesIO()
            img = img.convert('RGB')
            img.save(buffer, format='JPEG')  
            buffer.seek(0)
            processed_image = SimpleUploadedFile(
                uploaded_image_name, buffer.read(), content_type='image/jpeg'
            )

            user_profile.profile_picture = processed_image
            user_profile.save()

            return JsonResponse({'message': 'Image uploaded successfully.'})

    return JsonResponse({'error': 'Invalid request.'}, status=400)
