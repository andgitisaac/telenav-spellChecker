from rest_framework import serializers
from .models import UserQuery

class UserQuerySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserQuery 
        fields = ('pk','query', 'query_date')
