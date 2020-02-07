from django.contrib import admin
from django.urls import path
from download_url import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('actionUrl', views.download_btn, name='actionUrl'),
    # path('delete', views.download_btn, name='delete'),
    path('', views.homepage, name='home'),
    path('form', views.create_post, name='create_post'),

] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
