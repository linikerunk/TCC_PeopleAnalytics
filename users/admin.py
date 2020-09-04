from django.contrib import admin
from .models import Employee, CostCenter, Unity


@admin.register(Unity)
class UnityAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'name', 'email', 'unity', 'role', 'user']
    verbose_name = "Employee"
    verbose_name_plural = "Employees"


@admin.register(CostCenter)
class CostCenterAdmin(admin.ModelAdmin):
    list_display = ['number', 'name_department', 'responsible']