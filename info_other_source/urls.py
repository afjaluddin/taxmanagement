from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"), 
    path('', views.info_os_read, name='info_os_read'),
    path('<int:pk>/', views.info_os_update, name='info_os_update'),
    path('delete/<int:pk>/', views.info_os_delete, name='info_os_delete'), 
]