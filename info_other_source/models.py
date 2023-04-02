from django.db import models

# Create your models here.
class InfoOtherSource(models.Model):
    income_fixed_deposit = models.IntegerField(blank=True, null=True)
    income_share_divident = models.IntegerField(blank=True, null=True)
    inc_mutual_and_unit_fund = models.IntegerField(blank=True, null=True)
    technical_fees_income = models.IntegerField(blank=True, null=True)
    income_saving_acc = models.IntegerField(blank=True, null=True)
    rent_machinary_and_plant = models.IntegerField(blank=True, null=True)
    rent_furniture = models.IntegerField(blank=True, null=True)
    rent_land = models.IntegerField(blank=True, null=True)
    other_income_us33 = models.IntegerField(blank=True, null=True)