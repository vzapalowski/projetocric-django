from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import (
    Warning, Event, EventRoute, EventImage, EventHowknew, 
    EventForm, EventFormField, EventFormResponse, EventBond, Enrollment
)

@admin.register(Warning)
class WarningAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
    )

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1
    verbose_name = "Imagem do Evento"
    verbose_name_plural = "Imagens do Evento"

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

class EventRouteInline(admin.TabularInline):
    model = EventRoute
    extra = 1
    verbose_name = "Rota do Evento"
    verbose_name_plural = "Rotas do Evento"
    
    fieldsets = (
        (None, {
            'fields': (
                'route', 'name', 'active', 'time', 'concentration', 'departure_location'
            )
        }),
    )

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'status', 'location', 'form_link', 'created_at', 'banner_preview', 'enrollments_count', 'form_responses_count', 'routes_count')
    list_filter = ('status', 'date', 'created_at', 'form')
    search_fields = ('name', 'description', 'location', 'form__name')
    date_hierarchy = 'date'
    readonly_fields = ('created_at', 'updated_at', 'form_preview')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': (
                'name', 'description', 'form', 'form_preview', 'status'
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
        EventRouteInline,
        EventImageInline,
        AnchorpointInline,
        ParticipantsInline,
    ]
    
    def banner_preview(self, obj):
        if obj.banner_image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.banner_image.url)
        return "Sem imagem"
    banner_preview.short_description = 'Banner'
    
    def form_link(self, obj):
        if obj.form:
            url = reverse('admin:event_eventform_change', args=[obj.form.id])
            return format_html('<a href="{}">{}</a>', url, obj.form.name)
        return "Sem formulário"
    form_link.short_description = 'Formulário Vinculado'
    form_link.admin_order_field = 'form__name'
    
    def form_preview(self, obj):
        if obj.form:
            fields = obj.form.fields.all().order_by('order')
            if fields:
                html = '<h4>Campos do Formulário:</h4><ul style="margin-left: 20px;">'
                for field in fields:
                    required = " (Obrigatório)" if field.required else ""
                    html += f'<li><strong>{field.label}</strong> - {field.get_type_display()}{required}</li>'
                html += '</ul>'
                
                # Link para visualizar as respostas deste formulário no evento
                responses_url = reverse('admin:event_eventformresponse_changelist') + f'?enrollment__event__id__exact={obj.id}'
                html += f'<p><a href="{responses_url}" class="button">Ver Respostas deste Evento</a></p>'
                
                return format_html(html)
            return "Formulário sem campos definidos"
        return "Nenhum formulário vinculado"
    form_preview.short_description = 'Prévia do Formulário'
    
    def enrollments_count(self, obj):
        count = obj.enrollment_set.count()
        url = reverse('admin:event_enrollment_changelist') + f'?event__id__exact={obj.id}'
        return format_html('<a href="{}">{}</a>', url, count)
    enrollments_count.short_description = 'Inscrições'
    
    def form_responses_count(self, obj):
        count = EventFormResponse.objects.filter(enrollment__event=obj).count()
        url = reverse('admin:event_eventformresponse_changelist') + f'?enrollment__event__id__exact={obj.id}'
        return format_html('<a href="{}">{}</a>', url, count)
    form_responses_count.short_description = 'Respostas'
    
    def routes_count(self, obj):
        # Usando o related_name padrão do Django para ForeignKey
        count = EventRoute.objects.filter(event=obj).count()
        url = reverse('admin:event_eventroute_changelist') + f'?event__id__exact={obj.id}'
        return format_html('<a href="{}">{} Rotas</a>', url, count)
    routes_count.short_description = 'Rotas'

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
        if obj.image:  
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
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
    list_display = ('name', 'description', 'events_count', 'fields_count', 'responses_count')
    search_fields = ('name', 'description')
    
    inlines = [EventFormFieldInline]
    
    def fields_count(self, obj):
        return obj.fields.count()
    fields_count.short_description = 'Nº de Campos'
    
    def events_count(self, obj):
        count = Event.objects.filter(form__id=obj.id).count()
        url = reverse('admin:event_event_changelist') + f'?form__id__exact={obj.id}'
        return format_html('<a href="{}">{}</a>', url, count)
    events_count.short_description = 'Eventos Vinculados'
    
    def responses_count(self, obj):
        count = EventFormResponse.objects.filter(field__form=obj).count()
        url = reverse('admin:event_eventformresponse_changelist') + f'?field__form__id__exact={obj.id}'
        return format_html('<a href="{}">{}</a>', url, count)
    responses_count.short_description = 'Respostas'

@admin.register(EventFormField)
class EventFormFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'form', 'type', 'required', 'order', 'responses_count')
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
    
    def responses_count(self, obj):
        count = obj.eventformresponse_set.count()
        url = reverse('admin:event_eventformresponse_changelist') + f'?field__id__exact={obj.id}'
        return format_html('<a href="{}">{}</a>', url, count)
    responses_count.short_description = 'Respostas'

class EventFormResponseInline(admin.TabularInline):
    model = EventFormResponse
    extra = 0
    readonly_fields = ('field_name', 'field_type', 'formatted_value')
    fields = ('field_name', 'field_type', 'formatted_value')
    can_delete = False
    
    def field_name(self, obj):
        return obj.field.label or obj.field.name
    field_name.short_description = 'Campo'
    
    def field_type(self, obj):
        return obj.field.get_type_display()
    field_type.short_description = 'Tipo'
    
    def formatted_value(self, obj):
        return obj.value
    formatted_value.short_description = 'Resposta'
    
    def has_add_permission(self, request, obj=None):
        return False

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'route', 'created_at', 'form_responses_count')
    list_filter = ('event', 'route', 'created_at')
    search_fields = ('user__username', 'event__name', 'route__name')
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
    
    inlines = [EventFormResponseInline]
    
    def form_responses_count(self, obj):
        count = obj.responses.count()
        if count > 0:
            url = reverse('admin:event_eventformresponse_changelist') + f'?enrollment__id__exact={obj.id}'
            return format_html('<a href="{}">{}</a>', url, count)
        return count
    form_responses_count.short_description = 'Respostas do Formulário'

@admin.register(EventFormResponse)
class EventFormResponseAdmin(admin.ModelAdmin):
    list_display = ('enrollment_info', 'field_info', 'value_preview')
    list_filter = ('field__form', 'enrollment__event', 'field')
    search_fields = (
        'enrollment__user__username', 
        'enrollment__user__first_name', 
        'enrollment__user__last_name',
        'enrollment__event__name', 
        'field__name', 
        'value'
    )
    
    fieldsets = (
        (None, {
            'fields': (
                'enrollment', 'field', 'value'
            )
        }),
        ('Metadados', {
            'fields': (
                'created_at', 'updated_at'
            ),
            'classes': ('collapse',)
        }),
    )
    
    def enrollment_info(self, obj):
        url = reverse('admin:event_enrollment_change', args=[obj.enrollment.id])
        return format_html(
            '<a href="{}"><strong>{}</strong> - {}</a>', 
            url, 
            obj.enrollment.user.get_full_name() or obj.enrollment.user.username,
            obj.enrollment.event.name
        )
    enrollment_info.short_description = 'Inscrição'
    enrollment_info.admin_order_field = 'enrollment__user__first_name'
    
    def field_info(self, obj):
        return f"{obj.field.form.name} - {obj.field.label or obj.field.name}"
    field_info.short_description = 'Campo'
    field_info.admin_order_field = 'field__form__name'
    
    def value_preview(self, obj):
        if len(obj.value) > 100:
            return f"{obj.value[:100]}..."
        return obj.value
    value_preview.short_description = 'Resposta'
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related(
            'enrollment__user', 
            'enrollment__event', 
            'field__form'
        ).order_by('enrollment', 'field__order')
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ('created_at', 'updated_at')
        return ()