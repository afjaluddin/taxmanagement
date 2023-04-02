from django import forms
from django.db import models
from .models import InvestmentAllowance
from django.forms import fields, widgets

class InvestmentAllowanceForm(forms.ModelForm):
    # file_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}), required=True, error_messages={'required':'Must Enter a First Name'})
    class Meta:
        model = InvestmentAllowance
        fields = ['id','lip_premium','lip_value','pf_selfcont','pf_company_con','saf','benevolent_fund','group_insurance_pre','dps','investment_saving_cert','investment_icb','investment_gob_BandC','donation_gov_approve','investment_share_deb','investment_bond']
        widgets = {
            'lip_premium':forms.NumberInput(attrs={'class':'form-control'}),
            'lip_value':forms.NumberInput(attrs={'class':'form-control'}), 
            'pf_selfcont':forms.NumberInput(attrs={'class':'form-control'}),
            'pf_company_con':forms.NumberInput(attrs={'class':'form-control'}),
            'saf':forms.NumberInput(attrs={'class':'form-control'}),
            'benevolent_fund':forms.NumberInput(attrs={'class':'form-control'}),
            'group_insurance_pre':forms.NumberInput(attrs={'class':'form-control'}),
            'dps':forms.NumberInput(attrs={'class':'form-control'}),
            'investment_saving_cert':forms.NumberInput(attrs={'class':'form-control'}),
            'investment_icb':forms.NumberInput(attrs={'class':'form-control'}),
            'investment_gob_BandC':forms.NumberInput(attrs={'class':'form-control'}),
            'donation_gov_approve':forms.NumberInput(attrs={'class':'form-control'}),
            'investment_share_deb':forms.NumberInput(attrs={'class':'form-control'}),
            'investment_bond':forms.NumberInput(attrs={'class':'form-control'}),
        }