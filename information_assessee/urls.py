from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name="create"), 
    path('', views.info_ssessee_read, name='info_ssessee_read'),
    path('<int:pk>/', views.info_ssessee_update, name='info_ssessee_update'),
    path('delete/<int:pk>/', views.info_ssessee_delete, name='info_ssessee_delete'), 
]