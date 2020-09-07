from django.contrib import admin
from .models import BodyMassIndex


@admin.register(BodyMassIndex)
class UnityAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'weighing_date']
