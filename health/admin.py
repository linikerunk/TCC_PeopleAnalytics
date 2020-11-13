from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import BodyMassIndex, PeriodicExam


@admin.register(BodyMassIndex)
class BodyMassIndexAdmin(ImportExportModelAdmin):
    list_display = ['identifier', 'weighing_date', 'imc']


@admin.register(PeriodicExam)
class PeriodicExamViewAdmin(ImportExportModelAdmin):
    list_display = ['employee', 'exame', 'initial_date', 'final_date']
