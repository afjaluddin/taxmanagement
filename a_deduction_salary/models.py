from django.db import models
from information_assessee. models import InformationAssessee

# Create your models here.

class DeductionSalary(models.Model):
    name = models.ForeignKey(InformationAssessee, on_delete=models.CASCADE, blank=False)
    basic = models.IntegerField(blank=True, null=True)
    special_pay = models.IntegerField(blank=True, null=True)
    dearness_allowance = models.IntegerField(blank=True, null=True)
    conveyance_allowance = models.IntegerField(blank=True, null=True)
    houserent_allowance = models.IntegerField(blank=True, null=True)
    medical_allowance = models.IntegerField(blank=True, null=True)
    servant_allowance = models.IntegerField(blank=True, null=True)
    leave_allowance = models.IntegerField(blank=True, null=True)
    honorarium_reward_fees = models.IntegerField(blank=True, null=True)
    overtime_allowance = models.IntegerField(blank=True, null=True)
    bonus_Ex_gratia = models.IntegerField(blank=True, null=True)
    pf_employer = models.IntegerField(blank=True, null=True)
    accinterest_pf = models.IntegerField(blank=True, null=True)
    deemed_income_tran = models.IntegerField(blank=True, null=True)
    deemed_income_accr = models.IntegerField(blank=True, null=True)
    wwf = models.IntegerField(blank=True, null=True)
    fastival_bonus = models.IntegerField(blank=True, null=True)