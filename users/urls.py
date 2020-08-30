from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views # all views authentication
from users import views # every views that I put on the views.py

app_name = "users"


urlpatterns = [
    path('users/', views.UsersListView.as_view(), name="users_list"),
    path('user_create/', views.UsersCreateView.as_view(), name="user_create"),
    path('user_update/<int:id>/', views.UsersUpdateView.as_view(),
    name="user_update"),
    path('user_delete/<int:id>/', views.UsersDeleteView.as_view(),
    name="user_delete"),
    # Login and Logout
    path('', LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name="logout.html"),
    name="my_logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)