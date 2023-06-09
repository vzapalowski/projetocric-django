
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('cidades/', include('cities.urls')),
    path('eventos/', include('event.urls')),
    path('usuarios/', include('users.urls')),
    
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
