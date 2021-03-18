from django.urls import path
from .views import Home, accessUserStatuses, accessCompanies

urlpatterns = [
    path('', Home),
    path('user_status/', accessUserStatuses),
    path('company/', accessCompanies),
]