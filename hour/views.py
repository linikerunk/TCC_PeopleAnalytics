from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from hour.form import AbsenteeismRateForm
from users.models import Employee
from .models import AbsenteeismRate
import requests


def get_weather(param, url):
    r = requests.get(url)
    data = r.json()
    if param == 'today':
        prev = data['results']
    elif param == 'next_two_days':
        prev = data['results']['forecast'][1:3]
    elif param == 'next_four_days':
        prev = data['results']['forecast'][3:5]
    else:
        print('Parametro invalido!')
    return prev

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
            absenteeism = AbsenteeismRate.objects.last()
            print("form.absenteismo : ", form.data)
            messages.success(request, "Taxa de absenteismo calculada com sucesso!")
            context = {'form': form, 'employee': employee, 'absenteeism': absenteeism}
            return render(request, 'hour/index.html', context)
    context = {'form': form} 
    return render(request, 'hour/index.html', context)


def absenteeism_list(request):
    obj = AbsenteeismRate.objects.all().order_by('-id')
    paginator = Paginator(obj, 10)
    page = request.GET.get('page', 1)
    obj = paginator.get_page(page)
    context = {'obj': obj}
    return render(request, 'hour/list_absenteeism.html', context)


def fouls_forecast(request):
    if request.method == "POST":
        token = settings.API_TOKEN
        api_url = f"https://api.hgbrasil.com/weather?key={token}&city_name="
        city = request.POST.get('city', None)
        # try:
        url = api_url + city 
        context = {'today': get_weather('today', url),
                   'next_two_days': get_weather('next_two_days', url),
                   'next_four_days': get_weather('next_four_days', url),}
        return render(request, 'hour/fouls_forecast.html', context)
        # except Exception as e:
            # messages.error(request, "A cidade não é válida")
    return render(request, 'hour/index.html', {})
