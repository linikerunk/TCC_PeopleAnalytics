from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import View, TemplateView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.forms import formset_factory
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
from .forms import EvaluationSkillForm, SkillForm
from .models import Skill, EvaluationSkill, Evaluation

class IndexPerformance(TemplateView):
    template_name = 'performance/index.html'


class SkillView(CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'performance/create_a_ability.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        ability = request.POST.get('name')
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Habilidade {ability} adicionada com successo!')
        return render(request, self.template_name, {'form': form})


#TODO
class SkillInline(InlineFormSetFactory):
    model = Skill
    fields = ['name', 'description']

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


#TODO
class Evaluation(CreateWithInlinesView):
    model = Evaluation
    fields = ['valuator', 'rated', 'year', 'skill']


#TODO 
class EvaluationSkillView(CreateWithInlinesView):
    model = EvaluationSkill
    fields = ['evaluation', 'grade', 'skill']
    template_name = 'performance/evaluation.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        return render(request, self.template_name, {'form': form})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context