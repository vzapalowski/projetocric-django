from django.contrib import admin
from cities.models.city_image import CityImage


class CityImageAdmin(admin.StackedInline):
    model = CityImage

# admin.site.register(Image)
