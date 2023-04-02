from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"), 
    path('', views.info_hp_read, name='info_hp_read'),
    path('<int:pk>/', views.info_hp_update, name='info_hp_update'),
    path('delete/<int:pk>/', views.info_hp_delete, name='info_hp_delete'), 
]