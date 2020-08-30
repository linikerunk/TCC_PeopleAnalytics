from django.contrib import admin
from .models import Training, Entity, Instructor, Event


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['training_name', 'category', 'local']
    list_filter = ['training_name', 'category']


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ['entity_name', 'social_reason', 'cnpj']
    list_filter = ['entity_name', 'social_reason']


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['instructor_name', 'register_instructor']
    list_filter = ['instructor_name', 'register_instructor']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'value']
    list_filter = ['event_name', 'value']