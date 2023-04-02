from django import forms
from django.db import models
from .models import InformationSalary
from django.forms import fields, widgets

class InformationSalaryForm(forms.ModelForm):
    # file_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}), required=True, error_messages={'required':'Must Enter a First Name'})
    deemed_income_tran = forms.BooleanField(required=False)
    deemed_income_accr = forms.BooleanField(required=False)
    class Meta:
        model = InformationSalary
        fields = ['id','name', 'basic', 'special_pay', 'dearness_allowance', 'conveyance_allowance', 'houserent_allowance', 'medical_allowance', 'servant_allowance', 'leave_allowance', 'honorarium_reward_fees', 'overtime_allowance', 'bonus_Ex_gratia', 'pf_employer', 'accinterest_pf', 'deemed_income_tran', 'deemed_income_accr', 'wwf', 'fastival_bonus']
        widgets = {
            'name':forms.Select(attrs={'class':'form-control'}),
            'basic':forms.NumberInput(attrs={'class':'form-control'}), 
            'special_pay':forms.NumberInput(attrs={'class':'form-control'}),
            'dearness_allowance':forms.NumberInput(attrs={'class':'form-control'}),
            'conveyance_allowance':forms.NumberInput(attrs={'class':'form-control'}),
            'houserent_allowance':forms.NumberInput(attrs={'class':'form-control'}),
            'medical_allowance':forms.NumberInput(attrs={'class':'form-control'}),
            'servant_allowance':forms.NumberInput(attrs={'class':'form-control'}),
            'leave_allowance':forms.NumberInput(attrs={'class':'form-control'}),
            'honorarium_reward_fees':forms.NumberInput(attrs={'class':'form-control'}),
            'overtime_allowance':forms.NumberInput(attrs={'class':'form-control'}),
            'bonus_Ex_gratia':forms.NumberInput(attrs={'class':'form-control'}),
            'pf_employer':forms.NumberInput(attrs={'class':'form-control'}),
            'accinterest_pf':forms.NumberInput(attrs={'class':'form-control'}),
            'wwf':forms.NumberInput(attrs={'class':'form-control'}),
            'fastival_bonus':forms.NumberInput(attrs={'class':'form-control'}), 
        }