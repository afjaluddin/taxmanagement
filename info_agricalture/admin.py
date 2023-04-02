from django.contrib import admin
from .models import InfoAgricalture
# Register your models here.

# Register your models here.
@admin.register(InfoAgricalture)
class InfoAgricaltureAdmin(admin.ModelAdmin):
    list_display = ['income_from_sales', 'income_from_borga', 'income_from_processing', 'income_from_caltivation', 'total_agri_income', 'allowabe_exp', 'land_tax', 'interest_against_capital', 'other_exp_agri']