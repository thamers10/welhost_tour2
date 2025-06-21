from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.all_services_view, name="all_services"),
]
