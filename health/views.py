import datetime
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView, ListView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.urls import reverse_lazy
from utils.decorators import first_register
from .models import PeriodicExam, BodyMassIndex
from .forms import PeriodicExamForm, BodyMassIndexForm

UserModel = get_user_model()


@method_decorator(login_required, name='dispatch')
class PeriodicExamView(ListView):
    model = PeriodicExam
    template_name = 'health/periodic_exam.html'
    queryset = PeriodicExam.objects.all()
    context_object_name = 'exam'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PeriodicExamView, self).get_context_data(**kwargs)
        context['exams'] = PeriodicExam.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class IndexHealth(TemplateView):
    template_name = 'health/indice_mass.html'


@login_required
def create_period_exam(request):
    form = PeriodicExamForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        try:
            employee_clean = request.POST.get('employee')
            employee = Employee.objects.get(identifier=employee_clean)
        except Exception as e:
            print(request, 'Funcionário não encontrado.')
        if form.is_valid():
            form.save()
            messages.success(request, f'Exame do funcionário {employee.name}\
            cadastrado.')
            return redirect("health:create_exam")
        print("erro : ", form.errors)
    elif request.method == "GET":
        pass
    context = {'form' : form}
    return render(request, 'health/create_exam.html', context)


@login_required
def delete_period_exam(request, id):
    perido_exam = get_object_or_404(PeriodicExam, pk=id)
    if request.method == "DELETE":
        perido_exam.delete()
        # context['msg'] = "Periodo excluído com sucesso."
        messages.success(request, "Dado removido com sucesso!")
    else:
        return render(request, 'health/create_exam.html', {})
