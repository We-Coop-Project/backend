from rest_framework import serializers
from .models import User_status, Company, HireType

class HireTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HireType
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class UserStatusSerializer(serializers.ModelSerializer):
    company_statuses = CompanySerializer(many=True)
    class Meta:
        model = User_status
        fields = '__all__'
        depth = 1
    
    def create(self, validated_data):
        company_statuses_data = validated_data.pop('company_statuses')
        user_status = User_status.objects.create(**validated_data)
        user_status.save()
        
        for company_status_data in company_statuses_data:
            company = Company.objects.filter(name=company_status_data['name']).first()
            if company is None:
                company = Company.objects.create(**company_status_data)
            user_status.company_statuses.add(company)
        return user_status