from django.urls import path
from .views import Home, getAllCompanies

urlpatterns = [
    path('', Home),
    path('company/', getAllCompanies),
]