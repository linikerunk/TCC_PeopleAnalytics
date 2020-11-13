from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee, CostCenter, Unity
from .resources import *


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
    resource_class  =  CostCenterAdminResource
    list_display = ['number', 'name_department', 'responsible']