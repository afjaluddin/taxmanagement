from django import forms
from django.db import models
from .models import InfoHouseProperty
from django.forms import fields, widgets

class InfoHousePropertyForm(forms.ModelForm):
    class Meta:
        model = InfoHouseProperty
        fields = ['id', 'rental_income', 'allowable_rp', 'tax_municipal', 'land_revenue', 'interest_loan', 'insurance_premium', 'vacancy_allowance', 'interest_mortgage', 'capital_charge', 'other_exp']
        widgets = {
            'rental_income':forms.NumberInput(attrs={'class':'form-control'}),
            'allowable_rp':forms.NumberInput(attrs={'class':'form-control'}),
            'tax_municipal':forms.NumberInput(attrs={'class':'form-control'}),
            'land_revenue':forms.NumberInput(attrs={'class':'form-control'}),
            'interest_loan':forms.NumberInput(attrs={'class':'form-control'}),
            'insurance_premium':forms.NumberInput(attrs={'class':'form-control'}),
            'vacancy_allowance':forms.NumberInput(attrs={'class':'form-control'}),
            'interest_mortgage':forms.NumberInput(attrs={'class':'form-control'}),
            'capital_charge':forms.NumberInput(attrs={'class':'form-control'}),
            'other_exp':forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'allowable_rp': 'Allowable R&P',
        }