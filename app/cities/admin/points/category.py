
from django import forms
from django.contrib import admin

from cities.models import Category
    

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'city': forms.Select
        }


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name', )
    form = CategoryForm


admin.site.register(Category, CategoryAdmin)