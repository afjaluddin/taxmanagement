"""taxmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('information_assessee/', include('information_assessee.urls')),
    path('information_salary/', include('information_salary.urls')),
    path('info_house_property/', include('info_house_property.urls')),
    path('info_agricalture/', include('info_agricalture.urls')),
    path('info_other_source/', include('info_other_source.urls')),
    path('investment_allowance/', include('investment_allowance.urls')),
    path('deduction-salary/', include('a_deduction_salary.urls')),
    path('taxable-salary/', include('taxable_salary.urls')),
]
