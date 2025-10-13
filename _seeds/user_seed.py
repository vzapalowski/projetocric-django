from django.utils import timezone
from django.contrib.auth.models import User
from users.models import UserProfile
from datetime import date

def seed_users():
    users_data = [
        {
            'username': 'joao.silva',
            'email': 'joao.silva@email.com',
            'first_name': 'João',
            'last_name': 'Silva',
            'password': 'temp_password_123',
            'profile_data': {
                'birth_date': date(1990, 5, 15),
                'document': '123.456.789-00',
                'document_type': 'CPF',
                'social_network': '@joaosilva',
                'social_network_type': 'instagram',
                'profile_picture_path': 'profiles/joao_silva.jpg'
            }
        },
        {
            'username': 'maria.santos',
            'email': 'maria.santos@email.com',
            'first_name': 'Maria',
            'last_name': 'Santos',
            'password': 'temp_password_123',
            'profile_data': {
                'birth_date': date(1985, 8, 22),
                'document': '987.654.321-00',
                'document_type': 'CPF',
                'social_network': 'maria.santos',
                'social_network_type': 'facebook',
                'profile_picture_path': 'profiles/maria_santos.jpg'
            }
        }
    ]
    
    for user_data in users_data:
        profile_data = user_data.pop('profile_data')
        
        # Cria o usuário
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name']
        )
        
        # Cria o perfil
        UserProfile.objects.create(
            user=user,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            **profile_data
        )
    
    print("Users and profiles seeded successfully!")