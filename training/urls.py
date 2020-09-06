from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from training import views # every views that I put on the views.py

app_name = "training"


urlpatterns = [
    #### routes of Training ####
    path('training/', views.TrainingListView.as_view(),
    name="training_list"),
    path('training_create/', views.TrainingCreateView.as_view(),
    name="training_create"),
    path('training_update/<int:pk>/', views.TrainingUpdateView.as_view(),
    name="training_update"),
    path('training_delete/<int:pk>/', views.TrainingDeleteView.as_view(),
    name="training_delete"),
    #### routes of Entity ####
    path('entity/', views.EntityListView.as_view(),
    name="entity_list"),
    path('entity_create/', views.EntityCreateView.as_view(),
    name="entity_create"),
    path('entity_update/<int:pk>/', views.EntityUpdateView.as_view(),
    name="entity_update"),
    path('entity_delete/<int:pk>/', views.EntityDeleteView.as_view(),
    name="entity_delete"),
    #### routes of Instructor ####
    path('instructor/', views.InstructorListView.as_view(),
    name="instructor_list"),
    path('instructor_create/', views.InstructorCreateView.as_view(),
    name="instructor_create"),
    path('instructor_update/<int:pk>/', views.InstructorUpdateView.as_view(),
    name="instructor_update"),
    path('instructor_delete/<int:pk>/', views.InstructorDeleteView.as_view(),
    name="instructor_delete"),
    #### routes of Event ####
    path('event/', views.EventListView.as_view(),
    name="event_list"),
    path('event_create/', views.EventCreateView.as_view(),
    name="event_create"),
    path('event_update/<int:pk>/', views.EventUpdateView.as_view(),
    name="event_update"),
    path('event_delete/<int:pk>/', views.EventDeleteView.as_view(),
    name="event_delete"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)