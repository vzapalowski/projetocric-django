from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import CityManager


class CityManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'edit_city_link')

    def edit_city_link(self, obj):
         url = reverse('admin:cities_city_change', args=[obj.city.pk])
         return format_html('<a href="{}"> Editar cidade</a>', url)

    edit_city_link.short_description = 'Editar Cidade'

admin.site.register(CityManager, CityManagerAdmin)