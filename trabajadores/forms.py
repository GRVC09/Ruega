from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['datecontra','diasanotados','tiex']
        widgets = {
            'datecontra' : forms.DateInput(attrs={'class':'form-control'}),
            'diasanotados': forms.NumberInput(attrs={'class':'form-control'}),
            'tiex': forms.NumberInput(attrs={'class':'form-control'})
        }

#attrs={'class':'form-control'}