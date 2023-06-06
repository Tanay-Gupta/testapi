from rest_framework import serializers
from api.models import Leetcode,CodeChef




class LeetcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leetcode
        fields='__all__'

class CodeChefSerializer(serializers.ModelSerializer):
    class Meta:
        model=CodeChef
        fields='__all__'
        
