from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    RG = 'RG'; CPF = 'CPF';
    DOCUMENT_TYPES = [
        (RG, 'RG'),
        (CPF, 'CPF'),
    ]

    FACEBOOK = 'FACEBOOK'; INSTAGRAM = 'INSTAGRAM'; LINKEDIN = 'LINKEDIN'; OTHER = 'OTHER';
    SOCIAL_NETWORK_TYPES = [
        (FACEBOOK, 'Facebook'),
        (INSTAGRAM, 'Instagram'),
        (LINKEDIN, 'LinkedIn'),
        (OTHER, 'Outro')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birth_date = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    document = models.CharField(max_length=20, blank=True, null=True, verbose_name='Documento')
    document_type = models.CharField(max_length=3, choices=DOCUMENT_TYPES, blank=True, null=True, verbose_name='Tipo de Documento')
    social_network = models.CharField(max_length=255, blank=True, null=True, verbose_name='Rede Social')
    social_network_type = models.CharField(max_length=12, choices=SOCIAL_NETWORK_TYPES, blank=True, null=True, verbose_name='Tipo de Rede Social')
    profile_picture_path = models.ImageField(upload_to='users/images/%Y/%m/%d', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'user_profile'