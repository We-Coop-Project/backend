from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User_status, Company
from .serializers import UserStatusSerializer, CompanySerializer

def Home(request):
    return HttpResponse('<h1>Hello Django</h1>')

@api_view(['GET', 'POST'])
def accessUserStatuses(request):
    if request.method == 'GET':
        user_statuses = User_status.objects.all()
        serializer = UserStatusSerializer(user_statuses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def accessCompanies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # data = request.data
        # print(data)
        # new_companies = Company.objects.create(
        #     name=data['name'],
        #     start_date=data['start_date'],
        #     end_date=data['end_date'],
        # )
        # print(new_companies)
        # new_companies.save()

        # for user_status in data['user_statuses']:
        #     user_status_obj = User_status.objects.get(coop_start_date=user_status['coop_start_date'])
        #     new_companies.user_statuses.add(user_status_obj)
            
        serializer = CompanySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)