from django.contrib import admin
from .models import InfoOtherSource
# Register your models here.

# Register your models here.
@admin.register(InfoOtherSource)
class InfoOtherSourceAdmin(admin.ModelAdmin):
    list_display = ['income_fixed_deposit', 'income_share_divident', 'inc_mutual_and_unit_fund', 'technical_fees_income', 'income_saving_acc', 'rent_machinary_and_plant', 'rent_furniture', 'rent_land', 'other_income_us33']