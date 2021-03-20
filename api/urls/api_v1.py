from django.urls import path
from ..views.api_v1 import Home, accessAllUserStatuses, getUserStatus, accessAllCompanies, getCompany

urlpatterns = [
    path('', Home),
    path('user_status/', accessAllUserStatuses),
    path('user_status/<str:pk>/', getUserStatus),
    path('company/', accessAllCompanies),
    path('company/<str:pk>/', getCompany),
]