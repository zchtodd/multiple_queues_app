from django.urls import path
from . import views

urlpatterns = [
    path("fibonacci/", views.calculate_fibonacci, name="calculate_fibonacci"),
]
