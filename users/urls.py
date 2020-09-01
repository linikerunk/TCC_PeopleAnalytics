from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views # all views authentication
from users import views # every views that I put on the views.py

app_name = "users"


urlpatterns = [
    path('users/', views.EmployeeListView.as_view(), name="users_list"),
    path('user_create/', views.EmployeeCreateView.as_view(), name="user_create"),
    path('user_update/<int:id>/', views.EmployeeUpdateView.as_view(),
    name="user_update"),
    path('user_delete/<int:id>/', views.EmployeeDeleteView.as_view(),
    name="user_delete"),
    # Login and Logout
    path('', views.Login.as_view(
    template_name="registration/login.html"), name="login"),
    path("logout/",auth_views.LogoutView.as_view(
    template_name="registration/logout.html"), name="my_logout"),
    url(r'^register/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)