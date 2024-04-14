from django.contrib import admin
from django.urls import path, include
from devops.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('health', health_check, name='health_check'),
    path('', include('django_prometheus.urls')),
]
