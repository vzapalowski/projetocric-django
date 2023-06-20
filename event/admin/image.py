from django.contrib import admin
from event.models.image import Image


class ImageAdmin(admin.StackedInline):
    model = Image

# admin.site.register(Image)
