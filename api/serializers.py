from rest_framework import serializers
from api.models import *


class LeetcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leetcode
        fields = ['name', 'url', 'duration', 'start_time', 'end_time', 'status', 'in_24_hours']

class CodeChefSerializer(serializers.ModelSerializer):
    class Meta:
        model=CodeChef
        fields='__all__'

class CodeforcesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Codeforces
        fields='__all__'        

class CodingPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model=CodingPlatform
        fields='__all__'        

class AllContestsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AllContests
        fields='__all__'        


class HackerRankSerializer(serializers.ModelSerializer):
    class Meta:
        model=HackerRank
        fields='__all__'        


class HackerEarthSerializer(serializers.ModelSerializer):
    class Meta:
        model=HackerEarth
        fields='__all__'        


class CSAcademySerializer(serializers.ModelSerializer):
    class Meta:
        model=CSAcademy
        fields='__all__'        

class AtCoderSerializer(serializers.ModelSerializer):
    class Meta:
        model=AtCoder
        fields='__all__'        

class TopCoderSerializer(serializers.ModelSerializer):
    class Meta:
        model=TopCoder
        fields='__all__'        

class CodeForcesGymSerializer(serializers.ModelSerializer):
    class Meta:
        model=CodeForcesGym
        fields='__all__'        

class GeekforgeeksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Geekforgeeks
        fields='__all__'        

class CodingNinjasSerializer(serializers.ModelSerializer):
    class Meta:
        model=CodingNinjas
        fields='__all__'        

