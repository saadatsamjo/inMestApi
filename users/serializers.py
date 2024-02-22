# users/serializers.py
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.EmailField()

class CohortSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.TextField()
    year = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()

class CohortMemberSerializer(serializers.Serializer):
    cohort = CohortSerializer()
    member = UserSerializer()
    is_active = serializers.BooleanField(default=True)
    date_created = serializers.DateTimeField(auto_now_add=True)