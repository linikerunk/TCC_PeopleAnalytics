from django.conf import settings
from django import forms
from users.models import Employee
from .models import PeriodicExam, BodyMassIndex


class DateInput(forms.DateInput):
    input_type = 'date'


class PeriodicExamForm(forms.ModelForm):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())
    initial_date = forms.DateField(widget=DateInput)

    class Meta:
        model = PeriodicExam
        fields = ['employee', 'exame', 'initial_date']

    def clean_employee(self):
        data_employee = self.cleaned_data['employee']
        return data_employee
        

class BodyMassIndexForm(forms.ModelForm):

    class Meta:
        model = BodyMassIndex
        fields = ['identifier', 'weight', 'height',
        'abdominal_circumference', 'systolic_blood_pressure', 
        'diastolic_blood_pressure']
