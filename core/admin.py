# admin.py
from django.contrib import admin, messages
from django import forms
from django.utils.html import format_html
from django.conf import settings
import os
from .models import AnchorpointCategory, Anchorpoint, Route
from core.forms import RouteForm

# ===============================
# ANCHORPOINT CATEGORY ADMIN
# ===============================
class AnchorpointCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = AnchorpointCategory
        fields = '__all__'
    
    def clean_icon_name(self):
        icon_name = self.cleaned_data.get('icon_name')
        # Limpa o nome para ser válido como arquivo
        import re
        icon_name = re.sub(r'[^a-zA-Z0-9_-]', '', icon_name.lower())
        return icon_name

@admin.register(AnchorpointCategory)
class AnchorpointCategoryAdmin(admin.ModelAdmin):
    form = AnchorpointCategoryAdminForm
    list_display = ['name', 'icon_name', 'is_active', 'created_at', 'icon_preview', 'icon_status']
    list_editable = ['is_active']
    search_fields = ['name', 'icon_name']
    list_filter = ['is_active', 'created_at']
    readonly_fields = ['created_at', 'updated_at', 'icon_preview_large', 'icon_status']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'icon_name', 'is_active')
        }),
        ('Ícone', {
            'fields': ('icon_preview_large', 'icon_status')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    def icon_preview(self, obj):
        """Preview pequeno para lista"""
        if obj.icon_name:
            static_url = f"{settings.STATIC_URL}map-pins/{obj.icon_name}.svg"
            return format_html(
                '<img src="{}" width="32" height="32" alt="{}" style="border: 1px solid #ccc; border-radius: 4px;">',
                static_url, obj.icon_name
            )
        return "Sem ícone"
    icon_preview.short_description = 'Ícone'
    
    def icon_preview_large(self, obj):
        """Preview grande para edição"""
        if obj.icon_name:
            static_url = f"{settings.STATIC_URL}map-pins/{obj.icon_name}.svg"
            return format_html(
                '''
                <div style="text-align: center;">
                    <img src="{}" width="64" height="64" alt="{}" style="border: 1px solid #ddd; border-radius: 8px; padding: 4px;">
                    <p style="margin-top: 8px; font-size: 12px; color: #666;">{}.png</p>
                </div>
                ''',
                static_url, obj.icon_name, obj.icon_name
            )
        return "Sem ícone"
    icon_preview_large.short_description = 'Preview do Ícone'
    
    def icon_status(self, obj):
        """Mostra se o arquivo do ícone existe"""
        if obj.icon_name:
            icon_path = os.path.join(settings.STATIC_ROOT, 'map-pins', f"{obj.icon_name}.svg")
            print( icon_path )
            if os.path.exists(icon_path):
                return format_html('<span style="color: green;">✅ Arquivo encontrado</span>')
            else:
                return format_html('<span style="color: red;">❌ Arquivo não encontrado</span>')
        return "-"
    icon_status.short_description = 'Status do Arquivo'


# ===============================
# ANCHORPOINT ADMIN
# ===============================
class AnchorpointAdminForm(forms.ModelForm):
    class Meta:
        model = Anchorpoint
        fields = '__all__'
        widgets = {
            'business_hours': forms.TextInput(attrs={'placeholder': 'Ex: Seg-Sex: 08:00-18:00'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ex: (11) 99999-9999'}),
        }


@admin.register(Anchorpoint)
class AnchorpointAdmin(admin.ModelAdmin):
    form = AnchorpointAdminForm
    list_display = [
        'name', 
        'anchorpoint_category', 
        'city_display', 
        'active', 
        'is_event_anchorpoint',
        'image_preview'
    ]
    list_editable = ['active']
    list_filter = [
        'anchorpoint_category', 
        'active', 
        'is_event_anchorpoint',
        'anchorpoint_category__is_active'
    ]
    search_fields = ['name', 'address', 'anchorpoint_category__name']
    readonly_fields = ['image_preview_large', 'coordinates_display']
    fieldsets = (
        ('Informações Básicas', {
            'fields': (
                'name', 
                'anchorpoint_category', 
                'active',
                'is_event_anchorpoint'
            )
        }),
        ('Localização', {
            'fields': (
                'latitude', 
                'longitude',
                'coordinates_display',
                'address'
            )
        }),
        ('Contato e Horários', {
            'fields': (
                'phone',
                'business_hours'
            )
        }),
        ('Imagem', {
            'fields': (
                'image',
                'image_preview_large'
            )
        })
    )
    
    def image_preview(self, obj):
        """Preview pequeno da imagem na lista"""
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px; border: 1px solid #ddd;">',
                obj.image.url
            )
        return "-"
    image_preview.short_description = 'Imagem'
    
    def image_preview_large(self, obj):
        """Preview grande da imagem na edição"""
        if obj.image:
            return format_html(
                '''
                <div style="text-align: center;">
                    <img src="{}" width="200" height="150" style="object-fit: cover; border-radius: 8px; border: 1px solid #ddd;">
                    <p style="margin-top: 8px; font-size: 12px; color: #666;">{}</p>
                </div>
                ''',
                obj.image.url, obj.image.name
            )
        return "Nenhuma imagem cadastrada"
    image_preview_large.short_description = 'Preview da Imagem'
    
    def coordinates_display(self, obj):
        """Mostra coordenadas formatadas"""
        if obj.latitude and obj.longitude:
            return format_html(
                'Lat: {}<br>Lon: {}',
                obj.latitude, obj.longitude
            )
        return "Coordenadas não definidas"
    coordinates_display.short_description = 'Coordenadas Atuais'
    
    def city_display(self, obj):
        """Tenta extrair a cidade do endereço"""
        if obj.address:
            # Tenta pegar a última parte do endereço (geralmente a cidade)
            parts = obj.address.split(',')
            if len(parts) > 1:
                return parts[-1].strip()
        return "-"
    city_display.short_description = 'Cidade'
    
    # Ações personalizadas
    actions = ['activate_selected', 'deactivate_selected']
    
    def activate_selected(self, request, queryset):
        """Ativa os pontos selecionados"""
        updated = queryset.update(active=True)
        self.message_user(request, f'{updated} pontos de apoio ativados.')
    activate_selected.short_description = "Ativar pontos selecionados"
    
    def deactivate_selected(self, request, queryset):
        """Desativa os pontos selecionados"""
        updated = queryset.update(active=False)
        self.message_user(request, f'{updated} pontos de apoio desativados.')
    deactivate_selected.short_description = "Desativar pontos selecionados"

# ===============================
# ROUTE ADMIN
# ===============================
@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    form = RouteForm

    list_display = [
        'name',
        'external_strava_id',
        'distance',
        'active',
        'is_event_route',
        'color_preview',
    ]

    list_editable = ['active', 'is_event_route']
    search_fields = ['name', 'external_strava_id']
    list_filter = ['active', 'is_event_route']
    readonly_fields = ['polyline', 'distance']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': (
                'name',
                'external_strava_id',
                'active',
                'is_event_route',
                'color'
            )
        }),
        ('Dados da Rota', {
            'fields': (
                'distance',
                'polyline'
            )
        })
    )

    # This is for save polyline and distance before save the route in database    
    def save_model(self, request, obj, form, change):
        # _stra_details is from route forms
        details = getattr(form, "_strava_details", None)
        if details:
            obj.polyline = details["polyline"]
            obj.distance = str(details["distance"])
        super().save_model(request, obj, form, change)

    def color_preview(self, obj):
        return format_html(
            '<div style="width: 20px; height: 20px; background: {}; border: 1px solid #000; border-radius: 50%;"></div>',
            obj.color
        )
        
    color_preview.short_description = "Cor"

# ===============================
# CONFIGURAÇÕES GLOBAIS DO ADMIN
# ===============================
admin.site.site_header = 'Administração do Sistema de Mapas'
admin.site.site_title = 'Sistema de Mapas'
admin.site.index_title = 'Gerenciamento de Dados'

from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = 'Administração do Sistema de Mapas'
    site_title = 'Sistema de Mapas'
    index_title = 'Gerenciamento de Dados'

# Opcional: Se quiser ordenar os modelos de forma específica
def get_app_list(self, request):
    """
    Reorganiza a lista de apps no admin
    """
    app_dict = self._build_app_dict(request)
    
    app_ordering = {
        'auth': 1,
        'core': 2,
    }
    
    app_list = sorted(app_dict.values(), key=lambda x: app_ordering.get(x['app_label'], 999))
    
    for app in app_list:
        if app['app_label'] == 'core':  # Substitua pelo nome do seu app
            # Ordem dos modelos dentro do app
            model_ordering = {
                'anchorpointcategory': 1,
                'anchorpoint': 2,
                'route': 3,
            }
            app['models'].sort(key=lambda x: model_ordering.get(x['object_name'].lower(), 999))
    
    return app_list

admin.site.get_app_list = get_app_list.__get__(admin.site, AdminSite)