from django.db import models
import os

class AnchorpointCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    icon_name = models.CharField(max_length=100, unique=True, verbose_name='Nome do Ícone', help_text='Nome do arquivo sem extensão (ex: "restaurant", "museum")')

    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def icon_path(self):
        """Retorna o caminho do ícone - busca em static primeiro, depois em media"""
        static_path = f"images/map-pins/{self.icon_name}.png"
        media_path = f"categories/icons/{self.icon_name}.png"
        
        # Verifica se existe na pasta static (usando lógica de fallback)
        # Na prática, você sempre usará o caminho static
        return f"images/map-pins/{self.icon_name}.png"

    @property
    def icon_static_path(self):
        """Retorna o caminho completo para o arquivo estático"""
        from django.conf import settings
        return os.path.join(settings.STATIC_ROOT, 'images', 'map-pins', f"{self.icon_name}.png")

    class Meta:
        db_table = 'anchorpoint_category'
        verbose_name = 'Categoria de Ponto'
        verbose_name_plural = 'Categorias de Pontos'