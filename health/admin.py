from django.contrib import admin
from .models import BodyMassIndex, PeriodicExam


@admin.register(BodyMassIndex)
class BodyMassIndexAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'weighing_date', 'imc']


@admin.register(PeriodicExam)
class PeriodicExamViewAdmin(admin.ModelAdmin):
    list_display = ['employee', 'exame', 'initial_date', 'final_date']
