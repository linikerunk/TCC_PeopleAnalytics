""" This is a forms.py that helps to work on the payload of front-end """
from django.forms import ModelForm
from django.forms.widgets import TextInput
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms
from .models import Training, Entity, Instructor, Event


class TrainingForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = "__all__"


class EntityForm(forms.ModelForm):

    class Meta:
        model = Entity
        fields = "__all__"


class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = "__all__"


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = "__all__"