from django.db.models import fields
from django.forms import ModelForm, widgets
from statistic.models import *
from django import forms
from statistic.forms.function import *
class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = {'name', 'date_bday'}
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_bday': DateBirthday,    # forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Ism Familiya',
            'date_bday': 'Tug\'ilgan sana'
    

        }
    field_order = ['name', 'date_bday']

class StanokForm(ModelForm):
    class Meta:
        model = Stanok
        fields = {'title', 'number', 'workers', 'norma_value'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'workers': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'norma_value': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Nomi',
            'number': 'Nechinchi',
            'worker': 'Tegishli xodimlar',
            'norma_value': 'Norma atqi'
        }
    field_order = {'title', 'number', 'workers', 'norma_value'}

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = {'date', 'stanok', 'value', 'value2', 'value3'}
        widgets = {
            'date': DateReport,
            'stanok': forms.Select(attrs={'class': 'form-control'}), 
            'value': forms.TextInput(attrs={'class': 'form-control'}),
            # 'shift': forms.Select(attrs={'class': 'form-control'}, choices=[('1', '1'), ('2', '2'), ('3', '3')]),
            'value2': forms.TextInput(attrs={'class': 'form-control'}),
            'value3': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'date': 'Sana',
            'stanok': 'Stanok', 
            'value': 'Atqi 1-smena',
            'value2': 'Atqi 2-smena',
            'value3': 'Atqi 3-smena',
            
        }
    field_order = ['date', 'stanok', 'value', 'value2', 'value3']