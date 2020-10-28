from django.contrib import admin
from .models import AbsenteeismRate


@admin.register(AbsenteeismRate)
class AbsenteeismRateAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'days_month', 'absenteeism_days', 
                    'absenteeism', 'date_register']