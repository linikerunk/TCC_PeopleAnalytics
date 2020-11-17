import requests
import random
import scipy as sp
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


@login_required
def absenteeism_rate(request):
    form = AbsenteeismRateForm(request.POST or None)
    employee_field = request.POST.get('employee', None)
    employee = ''
    try:
        employee = Employee.objects.get(identifier=employee_field)
    except:
        print("Funcionário não encontrado.")
    if request.method == "POST":
        # validation 
        if request.POST.get('absenteeism_days', None) > request.POST.get('days_month', None):
            messages.error(request, "Dias de falta maiores do que dias existentes.")
            return render(request, 'hour/index.html', {})
        if form.is_valid():
            form.save()
            absenteeism = AbsenteeismRate.objects.last()
            print("form.absenteismo : ", form.data)
            messages.success(request, "Taxa de absenteismo calculada com sucesso!")
            context = {'form': form, 'employee': employee, 'absenteeism': absenteeism}
            return render(request, 'hour/index.html', context)
    context = {'form': form} 
    return render(request, 'hour/index.html', context)


@login_required
def absenteeism_list(request):
    obj = AbsenteeismRate.objects.all().order_by('-id')
    paginator = Paginator(obj, 10)
    page = request.GET.get('page', 1)
    obj = paginator.get_page(page)
    context = {'obj': obj}
    return render(request, 'hour/list_absenteeism.html', context)


@login_required
def fouls_forecast(request):
    employee = Employee.objects.all()
    if request.method == "POST":
        token = settings.API_TOKEN
        api_url = f"https://api.hgbrasil.com/weather?key={token}&city_name="
        city = request.POST.get('city', None)
        # try:
        url = api_url + city 
        context = {'today': get_weather('today', url),
                   'next_two_days': get_weather('next_two_days', url),
                   'next_four_days': get_weather('next_four_days', url),
                   'employee': employee}
        return render(request, 'hour/fouls_forecast.html', context)
        # except Exception as e:
            # messages.error(request, "A cidade não é válida")
    return render(request, 'hour/index.html', {'employee': employee})


@login_required
def list_hour_employee(request):
    obj = AbsenteeismRate.objects.all().filter(
        employee=request.user.employee.pk).order_by('-id')
    paginator = Paginator(obj, 10)
    page = request.GET.get('page', 1)
    obj = paginator.get_page(page)
    context = {'obj': obj}
    return render(request, 'hour/list_hour_employee.html', context)


@login_required
def verify_absent(request):
    name_employee = request.POST.get('employee', None)
    weather = request.POST.get('weather', None)
    try:
        employee = Employee.objects.get(name=str(name_employee))
    except Exception as e :
        messages.error(request, f'Erro : Colaborador não encontrado verifique o nome. {e}')
        return redirect('hour:hour')

    avegare_absenteism = []

    ##################################
    ##    Avegared Absenteism       ##
    ##################################
    for absenteeism in employee.rate_abis.all():
        absenteeism = float(str(absenteeism))
        print("Tipo absenteismo : ", type(absenteeism))
        avegare_absenteism.append(absenteeism)

    print("lista de absenteismo : ", avegare_absenteism)
    print("somatoria de absenteismo : ", sum(avegare_absenteism))
    avegare_absenteism = sum(avegare_absenteism) / len(avegare_absenteism)

    print("Média Absenteismo : ", avegare_absenteism)

    ############################################
    ##  Probability of Absenteeism Locomotion ##
    ############################################
    if employee.locomotion == 'Carro':
        print("Carro")
        s = sp.random.binomial(n=2, p=.3, size=31)
        prob_weather = avegare_absenteism * 0.20 * s  # chance of employee doesn't come to the company
        # prob_weather = [i for i in prob_weather if i != 0]
        rate_absenteism = random.choice(prob_weather)
    elif employee.locomotion == 'Moto':
        print("Moto")
        s = sp.random.binomial(n=4, p=.3, size=31)
        prob_weather = avegare_absenteism * 0.60 * s  # chance of employee doesn't come to the company
        # prob_weather = [i for i in prob_weather if i != 0]
        rate_absenteism = random.choice(prob_weather)
    elif employee.locomotion == 'Transporte Público':
        print("Transporte Público")
        s = sp.random.binomial(n=6, p=.3, size=31)
        prob_weather = avegare_absenteism * 0.75 * s
        # prob_weather = [i for i in prob_weather if i != 0]
        rate_absenteism = random.choice(prob_weather)
    elif employee.locomotion == 'Caminhada a pé':
        print("Caminhada a pé'")
        s = sp.random.binomial(n=8, p=.3, size=31)
        prob_weather = avegare_absenteism * 0.67 * s
        # prob_weather = [i for i in prob_weather if i != 0]
        rate_absenteism = random.choice(prob_weather)
    else:
        print("Erro, precisa ")
    
    ############################################
    ##  Probability of Absenteeism Weather    ##
    ############################################

    print("weather : ", weather)
    if weather == "Tempestade":
        print("Tempestade")
        rate_absenteism = rate_absenteism + 30 
    elif weather == "Chuva":
        print("Chuva")
        rate_absenteism = rate_absenteism + 17 
    elif weather == "Parcialmente nublado":
        print("Parcialmente nublado")
        rate_absenteism = rate_absenteism + 1 
    elif weather == "Trovoadas dispersas":
        print("Trovoadas dispersas")
        rate_absenteism = rate_absenteism + 20 
    elif weather == "Chuvas esparsas":
        print("Chuvas esparsas")
        rate_absenteism = rate_absenteism + 18 
    elif weather == "Tempo nublado":
        print("Tempo nublado")
        rate_absenteism = rate_absenteism + 2
    elif weather == "Ensolarado":
        print("Ensolarado")
        rate_absenteism = rate_absenteism + 3
    elif weather == "Sol com poucas nuvens":
        print("Sol com poucas nuvens")
        rate_absenteism = rate_absenteism + 1
    elif weather == "Chuviscos":
        print("Chuviscos")
        rate_absenteism = rate_absenteism + 7
    elif weather == "Alguns chuviscos":
        rate_absenteism = rate_absenteism + 7
    elif weather == "Tempo limpo":
        print("Tempo limpo")
        rate_absenteism = rate_absenteism + 0
    else:
        rate_absenteism = rate_absenteism + 3


    if rate_absenteism > 100:
        rate_absenteism = 100
    print("RATE ABSENTEISM : ", rate_absenteism)
    context = {'name_employee': name_employee,
               'weather': weather,
               'employee': employee,
               'avegare_absenteism': avegare_absenteism,
               'rate_absenteism': rate_absenteism,}
    
    return render(request, 'hour/absenteism.html', context)