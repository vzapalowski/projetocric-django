from django.contrib import admin
from cities.models import Route, Segment

class SegmentInline(admin.TabularInline):
    model = Segment
    fields = ('id', 'name', 'city', 'state', 'country', 'distance', 'total_elevation_gain', 'average_grade', 'elevation_low', 'effort_count', 'athlete_count', 'polyline', 'visible')
    extra = 0  

class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_route', 'active', 'polyline', 'distance')
    list_display_links = ('id', 'name', 'id_route', 'polyline', 'distance')
    readonly_fields = ('polyline', 'distance')
    inlines = [SegmentInline] 

admin.site.register(Route, RouteAdmin)