from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from hour import views # every views that I put on the views.py

app_name = "hour"


urlpatterns = [
    path('hour_management/', views.IndexHour.as_view(), name="hour"),
    path('hour_management/absenteeism_rate/', views.absenteeism_rate, 
    name="absenteeism_rate"),
    path('hour_management/absenteeism_list/', views.absenteeism_list,
    name="absenteeism_list"),
    path('hour_management/fouls_forecast/', views.fouls_forecast,
    name="fouls_forecast"),
    path('hour_management/list_hour_employee/', views.list_hour_employee,
    name="list_hour_employee"),
    path("hour_management/verify_absent/", views.verify_absent,
    name="verify_absent"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)