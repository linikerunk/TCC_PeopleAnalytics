from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from health import views # every views that I put on the views.py

app_name = "health"


urlpatterns = [
    path('health/', views.PeriodicExamView.as_view(), name="periodic_exam"),
    path('health/index_mass/', views.IndexHealth.as_view(), name="health"),
    path('health/create_exam/', views.create_period_exam, name="create_exam"),
    path('health/delete_period_exam/<int:id>/',
    views.delete_period_exam, name="delete_exam"),
    path('health/health_calculus/', views.health_calculus,
    name="health_calculus"),
    path('health/search_employee/', views.search_employee,
    name="search_employee"),
    path('health/list_index_body/', views.list_index_body,
    name="list_index_body")
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)