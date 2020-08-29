from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from health import views # every views that I put on the views.py

app_name = "health"


urlpatterns = [
    path('health/', views.IndexHealth.as_view()),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)