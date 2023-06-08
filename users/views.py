from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from event.models import Enrollment


def register(request):
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
        messages.error(request, 'As senhas informadas são diferentes')
        return render(request, 'users/register.html')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'Username já cadastrado')
        return render(request, 'users/register.html')

        
    messages.success(request, 'Usuario cadastrado com sucesso!')

    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    user.save()
    
    return render(request, 'users/register.html')

def login(request):
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
        return redirect('users:profile')

def logout(request):
    auth.logout(request)
    return redirect('users:login')

@login_required(login_url='users:login')
def profile(request):
    username = request.user.username

    email = request.user.email
    enrollments = Enrollment.objects.filter(email=email)

    return render(request,'users/profile.html', {'username': username, 'enrollments': enrollments})
