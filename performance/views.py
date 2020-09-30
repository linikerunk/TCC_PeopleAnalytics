from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import View, TemplateView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from extra_views import CreateWithInlinesView, InlineFormSet
from .forms import EvaluationSkillForm
from .models import Skill, EvaluationSkill

class IndexPerformance(TemplateView):
    template_name = 'performance/index.html'


class SkillInline(InlineFormSet):
    model = Skill


class EvaluationSkillView(CreateWithInlinesView):
    model = EvaluationSkill
    form_class = EvaluationSkillForm
    template_name = 'performance/evaluation.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        return render(request, self.template_name, {'form': form})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context