from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import View, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers
from ticket.forms import TicketForm
from users.models import Employee
from ticket.models import Category, SubCategory, Ticket, TicketHistory


def loading_subcategory(request, id):
    subcategory = SubCategory.objects.filter(category=id)
    data = serializers.serialize("json", subcategory, fields=('id', 'name'))
    response = {'data': data}
    return JsonResponse(response, safe=False)


def index_ticket(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'ticket/index.html', context)


def send_ticket(request):
    category = Category.objects.all()
    form = TicketForm(request.POST or None or request.FILE)
    category = request.POST.get('category', None)
    employee = Employee.objects.get(identifier=request.user.employee.identifier)
    context = {'form': form}
    if request.method == "POST":
        form.instance.employee = employee
        print("Form Data : ", form.data)
        print("Form Fields : ", form.fields)
        if form.is_valid():
            form.save()
            messages.success(request, f"Ticket {category} foi enviado com sucesso!")
            return render(request, 'ticket/index.html', context)
        print("Fiz um POST...", form.errors)
        return redirect('ticket:ticket')
    context = {'form': form, 'category': category, 'employee': employee}
    print("Fiz um GET...")
    return render(request, 'ticket/index.html', context)