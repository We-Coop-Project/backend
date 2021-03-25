from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models.api_v2 import UserStatus, Company
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
        user_statuses = UserStatus.objects.all()
        serializer = UserStatusSerializer(user_statuses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def accessUserStatus(request, pk):
    if request.method == 'GET':
        try: 
            user_status = UserStatus.objects.get(uid=pk)
        except UserStatus.DoesNotExist: 
            return JsonResponse({'message': 'The UserStatus does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserStatusSerializer(user_status, many=False)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        user_status = UserStatus.objects.get(uid=pk)
        serializer = UserStatusSerializer(instance=user_status, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def updateUserStatus(request, pk):
#     print(request.data)
#     user_status = UserStatus.objects.get(uid=pk)
#     serializer = UserStatusSerializer(instance=user_status, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


@api_view(['GET', 'POST'])
def accessCompany(request, pk):
    if request.method == 'GET':
        try: 
            company = Company.objects.get(id=pk)
        except Company.DoesNotExist: 
            return JsonResponse({'message': 'The Company does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(company, many=False)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        print(pk)
        company = Company.objects.get(id=pk)
        serializer = CompanySerializer(instance=company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# def getCompany(request, pk):
#     if request.method == 'GET':
#         user_status = User_status.objects.get(id=pk)
#         serializer = CompanySerializer(user_status, many=False)
#         print(serializer.data)
#         return Response(serializer.data)