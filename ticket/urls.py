from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from ticket import views # every views that I put on the views.py

app_name = "ticket"


urlpatterns = [
    path("reload_subcategory/<int:id>/",
    views.loading_subcategory, name="loading_subcategory"),
    path('tickets/', views.index_ticket, name="ticket"),
    path('tickets/list_ticket/', views.list_tickets, name="list_tickets"),
    path('tickets/send_ticket/', views.send_ticket, name="send_ticket"),
    path('tickets/finish_ticket/<int:id>/', views.finish_ticket, name="finish_ticket"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)