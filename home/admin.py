from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import CityManager
from .models.anchor_points_manager import AnchorPointsManager


class CityManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'edit_city_link')

    def edit_city_link(self, obj):
         url = reverse('admin:cities_city_change', args=[obj.city.pk])
         return format_html('<a href="{}"> Editar cidade</a>', url)

    edit_city_link.short_description = 'Editar Cidade'

class AnchorPointManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'anchor_point', 'edit_anchor_point_link')

    def edit_anchor_point_link(self, obj):
        url = reverse('admin:cities_anchorpoint_change', args=[obj.anchor_point.pk])
        return format_html('<a href="{}"> Editar Ponto</a>', url)
    
    edit_anchor_point_link.short_description = 'Editar Ponto'


admin.site.register(AnchorPointsManager, AnchorPointManagerAdmin)
admin.site.register(CityManager, CityManagerAdmin)
