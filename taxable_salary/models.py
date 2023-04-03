from django.db import models
from information_assessee. models import InformationAssessee
from information_salary .models import InformationSalary

# Create your models here.


class TaxableSalary(models.Model):
    name = models.ForeignKey(InformationAssessee, on_delete=models.CASCADE, blank=False)
    basic = models.IntegerField(blank=True, null=True)
    special_pay = models.IntegerField(blank=True, null=True)
    dearness_allowance = models.IntegerField(blank=True, null=True)
    conveyance_allowance = models.ForeignKey(InformationSalary, on_delete=models.CASCADE, related_name="conveyance_allowances")
    houserent_allowance = models.ForeignKey(InformationSalary, on_delete=models.CASCADE, related_name="houserent_allowances")
    medical_allowance = models.ForeignKey(InformationSalary, on_delete=models.CASCADE, related_name="medical_allowances")
    servant_allowance = models.IntegerField(blank=True, null=True)
    leave_allowance = models.IntegerField(blank=True, null=True)
    honorarium_reward_fees = models.IntegerField(blank=True, null=True)
    overtime_allowance = models.IntegerField(blank=True, null=True)
    bonus_Ex_gratia = models.IntegerField(blank=True, null=True)
    pf_employer = models.IntegerField(blank=True, null=True)
    accinterest_pf = models.ForeignKey(InformationSalary, on_delete=models.CASCADE, related_name="accinterest_pfs")
    deemed_income_tran = models.BooleanField(default=True)
    deemed_income_accr = models.BooleanField(default=True)
    wwf = models.ForeignKey(InformationSalary, on_delete=models.CASCADE, related_name="wwfs")
    fastival_bonus = models.IntegerField(blank=True, null=True)