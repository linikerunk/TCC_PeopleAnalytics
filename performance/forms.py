""" This is a forms.py that helps to work on the payload of front-end """
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import TextInput
from extra_views import ModelFormSetView, FormSetView
from .models import EvaluationSkill, Skill


class SkillForm(FormSetView):

    class Meta:
        model = Skill
        fields = '__all__'


class EvaluationSkillForm(ModelFormSetView):
    model = EvaluationSkill
    fields = ['evaluation', 'skill', 'grade']
    template_name = 'performance/evaluation.html'
