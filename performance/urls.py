from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from .views import (
performance,
SkillView # every views that I put on the views.py
)

app_name = "performance"


urlpatterns = [
    path('performance/', performance, name="performance_list"),
    path('performance/create_ability/', SkillView.as_view(),
    name="create_ability"),
    # path('performance/evaluation/', EvaluationView.as_view(),
    # name="evaluation"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)