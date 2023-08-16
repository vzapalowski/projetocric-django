from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from event.models import Enrollment, Bond, HowKnew, RoutePath
from datetime import datetime
from django.db import transaction
from .models import PersonalData


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
    
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = auth.authenticate(request, email=email, password=password)

    if not user:
        messages.error(request, 'Credenciais inválidas')
        return render(request, 'users/login.html')
    else:
        auth.login(request, user)
        request.session['user_id'] = user.id
        return redirect('users:profile')

def logout(request):
    auth.logout(request)
    return redirect('users:login')

@login_required(login_url='users:login')
def profile(request):
    
    user = User.objects.get(id=request.session.get('user_id'))

    email = user.email
    enrollments = Enrollment.objects.filter(email=email)

    return render(request,'users/profile.html', {'user': user, 'enrollments': enrollments})

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
