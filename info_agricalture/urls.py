from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name="create"), 
    path('', views.info_agri_read, name='info_agri_read'),
    path('<int:pk>/', views.info_agri_update, name='info_agri_update'),
    path('delete/<int:pk>/', views.info_agri_delete, name='info_agri_delete'),
]