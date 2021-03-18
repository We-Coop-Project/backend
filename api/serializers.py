from rest_framework import serializers
from .models import User_status, Company

class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_status
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    user_statuses = UserStatusSerializer(many=True)

    class Meta:
        model = Company
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        user_statuses_data = validated_data.pop('user_statuses')
        company = Company.objects.create(**validated_data)
        company.save()
        
        for user_status_data in user_statuses_data:
            user_status = User_status.objects.filter(working_time=user_status_data['working_time']).first()
            if user_status is None:
                user_status = User_status.objects.create(**user_status_data)
            company.user_statuses.add(user_status)
        return company