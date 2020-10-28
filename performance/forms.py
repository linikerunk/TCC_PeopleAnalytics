""" This is a forms.py that helps to work on the payload of front-end """
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.forms.widgets import TextInput
# from extra_views import ModelFormSetView, FormSetView
from .models import EvaluationSkill, Skill, Evaluation


class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = '__all__'


class EvaluationForm(forms.ModelForm):
    
    class Meta:
        model = Evaluation
        exclude = ()


class EvaluationSkillForm(forms.ModelForm):

    class Meta:
        model = EvaluationSkill
        exclude = ()

EvaluationSkillFormSet = inlineformset_factory(
    Evaluation, EvaluationSkill, form=EvaluationSkillForm,
    fields=['evaluation', 'skill', 'grade'], extra=1, can_delete=True
    )