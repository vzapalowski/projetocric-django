from django import forms
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from cities.models import AnchorPoint

class AnchorPointForm(forms.ModelForm):
    class Meta:
        model = AnchorPoint
        fields = '__all__'
        widgets = {
            'address': forms.Select,
            'category': forms.Select
        }
    

class AnchorPointAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'edit_category_link')
    list_display_links = ('id', 'name')

    def edit_category_link(self, obj):
        url = reverse('admin:cities_category_change', args=[obj.category.pk])
        return format_html('<a href="{}"> Editar Categoria</a>', url)

    edit_category_link.short_description = 'Editar Categoria'

admin.site.register(AnchorPoint, AnchorPointAdmin)