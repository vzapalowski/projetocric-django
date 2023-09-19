from django.contrib import admin
from event.models import Event, Image
from event.admin.event_form import EventForm
from event.admin.image import ImageAdmin
from event.models.anchor_point import AnchorPoint
from event.models.route_path import RoutePath
from event.models.enrollment_field import EnrollmentField
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile


class EventAdmin(admin.ModelAdmin):
    form = EventForm
    inlines = [ImageAdmin]
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    class Meta:
        model = Event

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "routes_data":
            kwargs["queryset"] = RoutePath.objects.filter(active=True)
        
        if db_field.name == "points":
            kwargs["queryset"] = AnchorPoint.objects.filter(active=True)

        if db_field.name == "enrollment_fields":
            kwargs["queryset"] = EnrollmentField.objects.all()

        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def save_related(self, request, form, formsets, change):
        instance = form.instance
        instance.users.clear()
        instance.users.add(*form.cleaned_data['users'])
        super().save_related(request, form, formsets, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(users=request.user)
        return qs

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if not request.user.is_superuser:
            fields = [field for field in fields if field != 'users']
        return fields
    
    def save_formset(self, request, form, formset, change):
        instance = form.instance
        super().save_formset(request, form, formset, change)


        if formset.model == Image:
            for image_obj in formset.save(commit=False):
                img = PILImage.open(image_obj.image.path)

                width, height = img.size
                size = min(width, height)
                left = (width - size) / 2
                top = (height - size) / 2
                right = (width + size) / 2
                bottom = (height + size) / 2
                img = img.crop((left, top, right, bottom))

                img = img.resize((300, 300)) 

                buffer = BytesIO()
                img.save(buffer, format='JPEG')  
                buffer.seek(0)
                new_image = SimpleUploadedFile(image_obj.image.name, buffer.read(), content_type='image/jpeg')
                
                
                image_obj.image = new_image
                image_obj.save()

admin.site.register(Event, EventAdmin)
