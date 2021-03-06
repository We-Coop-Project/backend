from django.urls import path
from ..views.api_v2 import Home, accessAllUserStatuses, accessUserStatus, accessAllCompanies, accessCompany

urlpatterns = [
    path('', Home),
    path('user_status/', accessAllUserStatuses),
    path('user_status/<str:pk>/', accessUserStatus),
    path('company/', accessAllCompanies),
    path('company/<str:pk>/', accessCompany),
]