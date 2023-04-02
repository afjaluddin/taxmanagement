from django import forms
from django.db import models
from .models import InformationAssessee
from django.forms import fields, widgets

class InformationAssesseeForm(forms.ModelForm):
    # file_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}), required=True, error_messages={'required':'Must Enter a First Name'})
    class Meta:
        model = InformationAssessee
        fields = ['id', 'file_name', 'name_assessee', 'birth_date', 'financial_year', 'assessment_year', 'employer', 'father_name', 'mother_name', 'spouse_name', 'nid', 'tin', 'circle_tax', 'zone_tax', 'email_personal', 'email_official', 'mobile_personal', 'mobile_official', 'address_present', 'address_permanent', 'gender', 'place', 'group_name']
        widgets = {
            'file_name':forms.TextInput(attrs={'class':'form-control'}), 
            'name_assessee':forms.TextInput(attrs={'class':'form-control'}),
            'birth_date' : forms.TextInput(attrs = {'class' : 'textinput form-control', 'type': 'date'}),
            'financial_year':forms.Select(attrs={'class':'form-control'}),
            'assessment_year':forms.Select(attrs={'class':'form-control'}),
            'employer':forms.TextInput(attrs={'class':'form-control'}),
            'father_name':forms.TextInput(attrs={'class':'form-control'}),
            'mother_name':forms.TextInput(attrs={'class':'form-control'}),
            'spouse_name':forms.TextInput(attrs={'class':'form-control'}),
            'nid':forms.TextInput(attrs={'class':'form-control'}),
            'tin':forms.TextInput(attrs={'class':'form-control'}),
            'circle_tax':forms.TextInput(attrs={'class':'form-control'}),
            'zone_tax':forms.TextInput(attrs={'class':'form-control'}),
            'email_personal':forms.EmailInput(attrs={'class':'form-control'}),
            'email_official':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile_personal':forms.TextInput(attrs={'class':'form-control'}),
            'mobile_official':forms.TextInput(attrs={'class':'form-control'}),
            'address_present':forms.TextInput(attrs={'class':'form-control'}),
            'address_permanent':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'place':forms.TextInput(attrs={'class':'form-control'}),
            'group_name':forms.TextInput(attrs={'class':'form-control'}), 
        }