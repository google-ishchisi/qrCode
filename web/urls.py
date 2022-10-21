from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from app.views import index, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('delete/<str:id>/', delete, name='delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
