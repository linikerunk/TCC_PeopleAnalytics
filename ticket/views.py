from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import View, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.utils import timezone
from django.core import serializers
from ticket.forms import TicketForm, TicketUpdateForm
from users.models import Employee
from ticket.models import Category, SubCategory, Ticket, TicketHistory


def loading_subcategory(request, id):
    subcategory = SubCategory.objects.filter(category=id)
    data = serializers.serialize("json", subcategory, fields=('id', 'name'))
    response = {'data': data}
    return JsonResponse(response, safe=False)


def index_ticket(request):
    category = Category.objects.all()
    form = TicketForm(request.POST or None)
    context = {'category': category, 'form': form}
    return render(request, 'ticket/index.html', context)


def send_ticket(request):
    category = Category.objects.all()
    employee = request.user.employee
    form = TicketForm(request.POST or None or request.FILES)
    category = request.POST.get('category', None)
    category_selected = Category.objects.get(id=category)
    context = {'form': form}
    if request.method == "POST":
        form.instance.employee = employee
        if form.is_valid():
            form.save()
            messages.success(request, f"Ticket da categoria {category_selected} \
            feito pelo funcionário {form.instance.employee} foi enviado com sucesso!")
            return redirect('ticket:ticket')
        return redirect('ticket:ticket')
    context = {'form': form, 'category': category, 'employee': employee}
    return render(request, 'ticket/index.html', context)


def list_tickets(request):
    tickets = Ticket.objects.all().order_by('-id')
    paginator = Paginator(tickets, 10)
    page = request.GET.get('page', 1)
    obj = paginator.get_page(page)
    return render(request, 'ticket/list_tickets.html', {'tickets': tickets,
                                                        'obj': obj})


def finish_ticket(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    employee = request.user.employee
    historic = TicketHistory.objects.filter(ticket__id=ticket.id)
    awnser = request.POST.get('awnser', None)
    context = {'ticket': ticket, 'employee': employee, 'historic': historic}
    if request.method == 'POST':
        form = TicketUpdateForm(
                request.POST,  request.FILES or None, instance=ticket)
        if form.is_valid():
            historic_ticket = TicketHistory.objects.create(
                date_message=timezone.now(),
                message=awnser,
                ticket_id=form.instance.id,
                employee=request.user.employee)
            historic_ticket.save()
            form.instance.awnser = ''
            form.save()
            messages.success(request, 'Chamado respondido com sucesso.')
            return redirect('ticket:list_tickets')

    return render(request, 'ticket/finish_tickets.html', context)