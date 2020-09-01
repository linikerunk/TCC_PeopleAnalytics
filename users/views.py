
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import SignupForm
from .tokens import account_activation_token
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

class Login(auth_views.LoginView):
    authentication_form = AuthenticationForm
    template_name= 'registration/login.html'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("I'm Here")
        return context

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Sua conta foi criada com sucesso no Enginee RH'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'registration/confirm_email.html')
    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'registration/acc_active_email.html')
    else:
        return HttpResponse('Link de ativação é inválido!')


@login_required
def my_logout(request):
    logout(request)
    return redirect('login')

