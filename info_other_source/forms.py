from django import forms
from django.db import models
from .models import InfoOtherSource
from django.forms import fields, widgets

class InfoOtherSourceForm(forms.ModelForm):
    class Meta:
        model = InfoOtherSource
        fields = ['id', 'income_fixed_deposit', 'income_share_divident', 'inc_mutual_and_unit_fund', 'technical_fees_income', 'income_saving_acc', 'rent_machinary_and_plant', 'rent_furniture', 'rent_land', 'other_income_us33']
        widgets = {
            'income_fixed_deposit':forms.NumberInput(attrs={'class':'form-control'}),
            'income_share_divident':forms.NumberInput(attrs={'class':'form-control'}),
            'inc_mutual_and_unit_fund':forms.NumberInput(attrs={'class':'form-control'}),
            'technical_fees_income':forms.NumberInput(attrs={'class':'form-control'}),
            'income_saving_acc':forms.NumberInput(attrs={'class':'form-control'}),
            'rent_machinary_and_plant':forms.NumberInput(attrs={'class':'form-control'}),
            'rent_furniture':forms.NumberInput(attrs={'class':'form-control'}),
            'rent_land':forms.NumberInput(attrs={'class':'form-control'}),
            'other_income_us33':forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'income_fixed_deposit': 'Inc Fixed Deposit',
            'income_share_divident': 'Inc Share Divident',
            'inc_mutual_and_unit_fund': 'Inc M&U Fund',
            # 'income_share_divident': 'Allowable R&P',
            # 'income_share_divident': 'Allowable R&P',
            # 'income_share_divident': 'Allowable R&P',
            # 'income_share_divident': 'Allowable R&P',
            # 'income_share_divident': 'Allowable R&P',
        }