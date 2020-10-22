from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee, CostCenter, Unity


@admin.register(Unity)
class UnityAdmin(ImportExportModelAdmin):
    list_display = ['name']


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    list_display = ['identifier', 'name', 'email', 'unity', 'role', 'user']
    verbose_name = "Employee"
    verbose_name_plural = "Employees"


@admin.register(CostCenter)
class CostCenterAdmin(ImportExportModelAdmin):
    list_display = ['number', 'name_department', 'responsible']