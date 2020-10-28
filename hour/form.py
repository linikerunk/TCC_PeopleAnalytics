from django.conf import settings
from django import forms
from users.models import Employee
from .models import AbsenteeismRate
        

class AbsenteeismRateForm(forms.ModelForm):

    class Meta:
        model = AbsenteeismRate

        fields = ['employee', 'absenteeism_days', 'days_month', ]
