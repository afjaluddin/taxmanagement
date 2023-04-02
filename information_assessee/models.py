from django.db import models
from django.utils.timezone import now
from django.db.models import CharField
from datetime import date
from datetime import datetime
# Create your models here.

class InformationAssessee(models.Model):
    file_name = models.CharField(max_length=64, blank=True)
    name_assessee = models.CharField(max_length=64, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    S_CHOICES = (
        ('2023-2024', '2023-2024'),
        ('2024-2025', '2024-2025'),
        ('2025-2026', '2025-2026'),
        ('2026-2027', '2026-2027'),
        ('2027-2028', '2027-2028'),
        ('2028-2029', '2028-2029'),
        ('2029-2030', '2029-2030'),
        ('2030-2031', '2030-2031'),
        ('2031-2032', '2031-2032'),
        ('2032-2033', '2032-2033'),
    )
    financial_year = CharField(max_length=32, blank=True, choices=S_CHOICES)
    assessment_year = CharField(max_length=32, blank=True, choices=S_CHOICES)
    employer = models.CharField(max_length=64, blank=True)
    father_name = models.CharField(max_length=64, blank=True)
    mother_name = models.CharField(max_length=64, blank=True)
    spouse_name = models.CharField(max_length=64, blank=True)
    nid = models.CharField(max_length=64, blank=True)
    tin = models.CharField(max_length=64, blank=True)
    circle_tax = models.CharField(max_length=64, blank=True)
    zone_tax = models.CharField(max_length=64, blank=True)
    email_personal = models.EmailField(max_length=64, blank=True, unique=True)
    email_official = models.EmailField(max_length=64, blank=True, unique=True)
    mobile_personal = models.CharField(max_length=32, blank=True)
    mobile_official = models.CharField(max_length=32, blank=True)
    address_present = models.CharField(max_length=256, blank=True)
    address_permanent = models.CharField(max_length=256, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    place = models.CharField(max_length=32, blank=True)
    group_name = models.CharField(max_length=32, blank=True)
    
    def __str__(self):
        return self.name_assessee
    
    def age(self):
        today = date.today()
        years_difference = today.year - self.birth_date.year
        is_before_birthday = (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        if is_before_birthday:
            return years_difference - 1
        return years_difference