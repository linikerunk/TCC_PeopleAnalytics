from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from .views import IndexPerformance, EvaluationSkillView, SkillView # every views that I put on the views.py

app_name = "performance"


urlpatterns = [
    path('performance/', IndexPerformance.as_view(),
    name="performance_list"),
    path('performance/evaluation/', EvaluationSkillView.as_view(),
    name="evaluation"),
    path('performance/create_ability/', SkillView.as_view(),
    name="create_ability"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)