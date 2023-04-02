from django.contrib import admin
from .models import InformationAssessee
# Register your models here.

# Register your models here.
@admin.register(InformationAssessee)
class InformationAssesseeAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'name_assessee', 'birth_date', 'financial_year', 'assessment_year', 'employer', 'father_name', 'mother_name', 'spouse_name', 'nid', 'tin', 'circle_tax', 'zone_tax', 'email_personal', 'email_official', 'mobile_personal', 'mobile_official', 'address_present', 'address_permanent', 'gender', 'place', 'group_name']