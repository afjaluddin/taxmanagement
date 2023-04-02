from django.db import models

# Create your models here.

class InfoAgricalture(models.Model):
    income_from_sales = models.IntegerField(blank=True, null=True)
    income_from_borga = models.IntegerField(blank=True, null=True)
    income_from_processing = models.IntegerField(blank=True, null=True)
    income_from_caltivation = models.IntegerField(blank=True, null=True)
    total_agri_income = models.IntegerField(blank=True, null=True)
    allowabe_exp = models.IntegerField(blank=True, null=True)  # 60%
    land_tax = models.IntegerField(blank=True, null=True)
    interest_against_capital = models.IntegerField(blank=True, null=True)
    other_exp_agri = models.IntegerField(blank=True, null=True)