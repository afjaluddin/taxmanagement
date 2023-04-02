from django.db import models

# Create your models here.

class InfoHouseProperty(models.Model):
    rental_income = models.IntegerField(blank=True, null=True)
    allowable_rp = models.IntegerField(blank=True, null=True)
    tax_municipal = models.IntegerField(blank=True, null=True)
    land_revenue = models.IntegerField(blank=True, null=True)
    interest_loan = models.IntegerField(blank=True, null=True)
    insurance_premium = models.IntegerField(blank=True, null=True)
    vacancy_allowance = models.IntegerField(blank=True, null=True)
    interest_mortgage = models.IntegerField(blank=True, null=True)
    capital_charge = models.IntegerField(blank=True, null=True)
    other_exp = models.IntegerField(blank=True, null=True)