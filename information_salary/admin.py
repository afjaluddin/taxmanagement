from django.contrib import admin
from .models import InformationSalary
# Register your models here.


@admin.register(InformationSalary)
class InformationSalaryAdmin(admin.ModelAdmin):
    list_display = ['name', 'basic', 'special_pay', 'dearness_allowance', 'conveyance_allowance', 'houserent_allowance', 'medical_allowance', 'servant_allowance', 'leave_allowance', 'honorarium_reward_fees', 'overtime_allowance', 'bonus_Ex_gratia', 'pf_employer', 'accinterest_pf', 'deemed_income_tran', 'deemed_income_accr', 'wwf', 'fastival_bonus']