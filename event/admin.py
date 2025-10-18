from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.html import format_html
from .models import (
    Warning, Event, EventRoute, EventImage, EventHowknew, 
    EventForm, EventFormField, EventFormResponse, EventBond, Enrollment
)

@admin.register(Warning)
class WarningAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
    )

# class EventRouteInline(admin.TabularInline):
#     model = Event.route.through
#     extra = 1
#     verbose_name = "Rota do Evento"
#     verbose_name_plural = "Rotas do Evento"

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1
    verbose_name = "Imagem do Evento"
    verbose_name_plural = "Imagens do Evento"

# class WarningInline(admin.TabularInline):
#     model = Event.warning.through
#     extra = 1
#     verbose_name = "Aviso"
#     verbose_name_plural = "Avisos"

class AnchorpointInline(admin.TabularInline):
    model = Event.anchorpoint.through
    extra = 1
    verbose_name = "Ponto de Âncora"
    verbose_name_plural = "Pontos de Âncora"

class ParticipantsInline(admin.TabularInline):
    model = Event.participants.through
    extra = 1
    verbose_name = "Participante"
    verbose_name_plural = "Participantes"

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'status', 'location', 'created_at', 'banner_preview')
    list_filter = ('status', 'date', 'created_at')
    search_fields = ('name', 'description', 'location')
    date_hierarchy = 'date'
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': (
                'name', 'description', 'form', 'status'
            )
        }),
        ('Datas', {
            'fields': (
                'date', 'secondary_date'
            )
        }),
        ('Localização', {
            'fields': (
                'latitude', 'longitude', 'location', 'zoom'
            )
        }),
        ('Arquivos', {
            'fields': (
                'banner_image', 'pdf_file'
            )
        }),
        ('Metadados', {
            'fields': (
                'created_at', 'updated_at'
            ),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [
        EventImageInline,
        AnchorpointInline,
        ParticipantsInline,
    ]
    
    def banner_preview(self, obj):
        if obj.banner_image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.banner_image.url)
        return "Sem imagem"
    banner_preview.short_description = 'Banner'

@admin.register(EventRoute)
class EventRouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'route', 'time', 'departure_location', 'active')
    list_filter = ('active', 'event', 'route')
    search_fields = ('name', 'departure_location', 'event__name')
    list_editable = ('active',)
    
    fieldsets = (
        (None, {
            'fields': (
                'event', 'route', 'name', 'active'
            )
        }),
        ('Horários e Local', {
            'fields': (
                'time', 'concentration', 'departure_location'
            )
        }),
    )

@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display = ('event', 'image_preview')
    list_filter = ('event',)
    search_fields = ('event__name',)
    
    def image_preview(self, obj):
        if obj.image_path:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image_path.url)
        return "Sem imagem"
    image_preview.short_description = 'Preview'

@admin.register(EventHowknew)
class EventHowknewAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(EventBond)
class EventBondAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class EventFormFieldInline(admin.TabularInline):
    model = EventFormField
    extra = 1
    ordering = ('order',)
    
    fieldsets = (
        (None, {
            'fields': (
                'name', 'label', 'type', 'required', 'options', 'validation', 'order'
            )
        }),
    )

@admin.register(EventForm)
class EventFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'fields_count')
    search_fields = ('name', 'description')
    
    inlines = [EventFormFieldInline]
    
    def fields_count(self, obj):
        return obj.fields.count()
    fields_count.short_description = 'Nº de Campos'

@admin.register(EventFormField)
class EventFormFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'form', 'type', 'required', 'order')
    list_filter = ('type', 'required', 'form')
    search_fields = ('name', 'label', 'form__name')
    list_editable = ('order',)
    
    fieldsets = (
        (None, {
            'fields': (
                'form', 'name', 'label', 'type', 'required', 'order'
            )
        }),
        ('Configurações Avançadas', {
            'fields': (
                'options', 'validation'
            ),
            'classes': ('collapse',)
        }),
    )

@admin.register(EventFormResponse)
class EventFormResponseAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'field', 'value_preview')
    list_filter = ('field__form', 'field')
    search_fields = ('enrollment__user__username', 'enrollment__event__name', 'field__name', 'value')
    
    def value_preview(self, obj):
        if len(obj.value) > 50:
            return f"{obj.value[:50]}..."
        return obj.value
    value_preview.short_description = 'Valor'

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'route', 'created_at')
    list_filter = ('event', 'route', 'created_at')
    search_fields = ('user__username', 'event__name', 'route__name')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': (
                'user', 'event', 'route'
            )
        }),
        ('Metadados', {
            'fields': (
                'created_at', 'updated_at'
            ),
            'classes': ('collapse',)
        }),
    )