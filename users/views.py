from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Employee, Unity, CostCenter

""" All classes that references a Users """
@method_decorator(login_required, name='dispatch')
class EmployeeListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'user'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        user = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(user, self.paginate_by)
        try:
            user = paginator.page(page)
        except PageNotAnInteger:
            user = paginator.page(1)
        except EmptyPage:
            user = paginator.page(paginator.num_pages)
        context['user'] = user
        return context


@method_decorator(login_required, name='dispatch')
class EmployeeCreateView(CreateView):
    model = User
    template_name = 'users/user_create.html'
    fields = '__all__'
    success_url = reverse_lazy('users_list')


@method_decorator(login_required, name='dispatch')
class EmployeeUpdateView(UpdateView):
    model = User
    template_name = 'users/user_update.html'
    fields = '__all__'
    success_url = reverse_lazy('users_list')


@method_decorator(login_required, name='dispatch')
class EmployeeDeleteView(DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('users-list')


# Login and Logout..
def login(request):
    context = {}
    return render(request, 'login.html', context)


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user, backend=None)
            return render(request, 'login.html', context)
    context['form'] = form
    return render(request, 'registration/register.html', context)


@login_required
def my_logout(request):
    logout(request)
    return redirect('login')

