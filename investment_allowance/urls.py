from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name="create"), 
    path('', views.investment_allowance_read, name='investment_allowance_read'),
    path('<int:pk>/', views.investment_allowance_update, name='investment_allowance_update'),
    path('delete/<int:pk>/', views.investment_allowance_delete, name='investment_allowance_delete'),
]