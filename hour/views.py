from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from hour.form import AbsenteeismRateForm
from users.models import Employee
import requests


class IndexHour(TemplateView):
    # model = 
    template_name = 'hour/index.html'

    def get(self, request, *args, **kwargs):
        nome_cidade = request.POST.get('cidade')
        tempo = requests.get(f"https://api.hgbrasil.com/weather?key=32e5ba65&city_name={nome_cidade}")
        print("Dados Tempo : ", tempo.json())
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


def absenteeism_rate(request):
    form = AbsenteeismRateForm(request.POST or None)
    employee_field = request.POST.get('employee', None)
    employee = ''
    try:
        employee = Employee.objects.get(identifier=employee_field)
    except:
        print("Funcionário não encontrado.")
    if request.method == "POST":
        if form.is_valid():
            form.save()
            print("form.absenteismo : ", form.data)
            messages.success(request, "Taxa de absenteismo calculada com sucesso!")
            context = {'form': form, 'employee': employee}
            return render(request, 'hour/index.html', context)
    context = {'form': form} 
    return render(request, 'hour/index.html', context)
