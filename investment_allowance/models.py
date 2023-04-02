from django.db import models

# Create your models here.

class InvestmentAllowance(models.Model):
    lip_premium = models.IntegerField(blank=True, null=True)
    lip_value = models.IntegerField(blank=True, null=True)
    pf_selfcont = models.IntegerField(blank=True, null=True)
    pf_company_con = models.IntegerField(blank=True, null=True)
    saf = models.IntegerField(blank=True, null=True)
    benevolent_fund = models.IntegerField(blank=True, null=True)
    group_insurance_pre = models.IntegerField(blank=True, null=True)
    dps = models.IntegerField(blank=True, null=True)
    investment_saving_cert = models.IntegerField(blank=True, null=True)
    investment_icb = models.IntegerField(blank=True, null=True)
    investment_gob_BandC = models.IntegerField(blank=True, null=True)
    donation_gov_approve = models.IntegerField(blank=True, null=True)
    investment_share_deb = models.IntegerField(blank=True, null=True)
    investment_bond = models.IntegerField(blank=True, null=True)