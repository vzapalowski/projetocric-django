from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType

def seed_auth_data():
    # Criar grupos
    admin_group, _ = Group.objects.get_or_create(name='Administradores')
    manager_group, _ = Group.objects.get_or_create(name='Gerentes')
    user_group, _ = Group.objects.get_or_create(name='Usuários')
    
    # Adicionar usuários aos grupos
    users = User.objects.all()
    for i, user in enumerate(users):
        if i == 0:  # Primeiro usuário como admin
            user.groups.add(admin_group)
        elif i == 1:  # Segundo como gerente
            user.groups.add(manager_group)
        else:  # Restante como usuários comuns
            user.groups.add(user_group)
    
    print("Auth groups and permissions seeded successfully!")