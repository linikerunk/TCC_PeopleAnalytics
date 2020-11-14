from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import View, TemplateView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import formset_factory
# from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
from .forms import EvaluationSkillForm, SkillForm, EvaluationForm
from .models import Skill, EvaluationSkill, Evaluation

def performance(request):
    if request.user.employee.role != "RH":
        return render(request, 'registration/denied_permission.html', {})
    return render(request, 'performance/index.html', {})


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

# class EvaluationView(CreateView):
#     model = Evaluation
#     form_class = EvaluationForm
#     template_name = 'performance/evaluation.html'
#     success_url = None

#     def get_context_data(self, **kwargs):
#         data = super(EvaluationView, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['evaluations'] = EvaluationSkillForm(self.request.POST)
#         else:
#             data['evaluations'] = EvaluationSkillForm()
#         return data

#     def form_valid(self, form):
#         context = self.get_context_data()
#         evaluations = context['evaluations']
#         with transaction.atomic():
#             form.instance.created_by = self.request.user
#             self.object = form.save()
#             if evaluations.is_valid():
#                 evaluations.instance = self.object
#                 evaluations.save()
#         return super(EvaluationView, self).form_valid(form)

