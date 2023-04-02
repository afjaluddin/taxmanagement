from django import forms
from django.db import models
from .models import InfoAgricalture
from django.forms import fields, widgets

class InfoAgricaltureForm(forms.ModelForm):
    class Meta:
        model = InfoAgricalture
        fields = ['id', 'income_from_sales', 'income_from_borga', 'income_from_processing', 'income_from_caltivation', 'total_agri_income', 'allowabe_exp', 'land_tax', 'interest_against_capital', 'other_exp_agri']
        widgets = {
            'income_from_sales':forms.NumberInput(attrs={'class':'form-control'}),
            'income_from_borga':forms.NumberInput(attrs={'class':'form-control'}),
            'income_from_processing':forms.NumberInput(attrs={'class':'form-control'}),
            'income_from_caltivation':forms.NumberInput(attrs={'class':'form-control'}),
            'total_agri_income':forms.NumberInput(attrs={'class':'form-control'}),
            'allowabe_exp':forms.NumberInput(attrs={'class':'form-control'}),
            'land_tax':forms.NumberInput(attrs={'class':'form-control'}),
            'interest_against_capital':forms.NumberInput(attrs={'class':'form-control'}),
            'other_exp_agri':forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'income_from_sales': 'Income Sales',
            'income_from_borga': 'Income Borga',
            'income_from_processing': 'Income Processing',
            'income_from_caltivation': 'Income Caltivation',
            'total_agri_income': 'Total Income',
            'allowabe_exp': 'Allowabe Exp',
            'land_tax': 'Land Tax',
            'interest_against_capital': 'Interest Against Capital',
            'other_exp_agri': 'Other Exp Agri',
        }