from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name="create"), 
    path('', views.info_salary_read, name='info_salary_read'),
    path('<int:pk>/', views.info_salary_update, name='info_salary_update'),
    path('delete/<int:pk>/', views.info_salary_delete, name='info_salary_delete'),
]