from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models.api_v2 import User_status, Company
from ..serializers.api_v2 import UserStatusSerializer, CompanySerializer

@api_view(['GET'])
def Home(request):
    api_url = {
        '/user_status': 'Get all user_statuses and Create a new user_status',
        '/user_status/<str:pk>': 'Get specific user_statuses',
        '/company': 'Get all companies and Create a new company',
        '/company/<str:pk>': 'Get specific company',
    }
    return Response(api_url)

@api_view(['GET', 'POST'])
def accessAllUserStatuses(request):
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


@api_view(['GET'])
def getUserStatus(request, pk):
    user_statuses = User_status.objects.get(uid=pk)
    serializer = UserStatusSerializer(user_statuses, many=False)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def accessAllCompanies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getCompany(request, pk):
    if request.method == 'GET':
        companies = Company.objects.get(id=pk)
        serializer = CompanySerializer(companies, many=False)
        print(serializer.data)
        return Response(serializer.data)