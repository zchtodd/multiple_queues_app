from django.urls import path
from . import views

urlpatterns = [
    path("fibonacci/", views.calculate_fibonacci, name="calculate_fibonacci"),
    path("prime/", views.calculate_prime, name="calculate_prime"),
]
