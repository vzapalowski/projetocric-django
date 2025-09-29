from django import forms
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from cities.models import City, Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'city': forms.Select
        }


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'street_name', 'number', 'edit_city_link')
    list_display_links = ('id', 'street_name',)
    form = AddressForm


    def edit_city_link(self, obj):
         url = reverse('admin:cities_city_change', args=[obj.city.pk])
         return format_html('<a href="{}"> Editar cidade</a>', url)

    edit_city_link.short_description = 'Editar Cidade'

admin.site.register(Address, AddressAdmin)
    
