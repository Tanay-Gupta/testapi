from django.shortcuts import render,HttpResponse
from rest_framework import viewsets

from api.models import *
from api.serializers import *



class LeetcodeViewSet(viewsets.ModelViewSet):
    queryset=Leetcode.objects.all().exclude('id')
    serializer_class=LeetcodeSerializer 

class CodeChefViewSet(viewsets.ModelViewSet):
    queryset=CodeChef.objects.all()
    serializer_class=CodeChefSerializer     

class CodeforcesViewSet(viewsets.ModelViewSet):
    queryset=Codeforces.objects.all()
    serializer_class=CodeforcesSerializer    

class CodingPlatformViewSet(viewsets.ModelViewSet):
    queryset=CodingPlatform.objects.all()
    serializer_class=CodingPlatformSerializer   

class AllContestsViewSet(viewsets.ModelViewSet):
    queryset = AllContests.objects.all()
    serializer_class = AllContestsSerializer

class HackerRankViewSet(viewsets.ModelViewSet):
    queryset = HackerRank.objects.all()
    serializer_class = HackerRankSerializer

class HackerEarthViewSet(viewsets.ModelViewSet):
    queryset = HackerEarth.objects.all()
    serializer_class = HackerEarthSerializer

class CSAcademyViewSet(viewsets.ModelViewSet):
    queryset = CSAcademy.objects.all()
    serializer_class = CSAcademySerializer

class AtCoderViewSet(viewsets.ModelViewSet):
    queryset = AtCoder.objects.all()
    serializer_class = AtCoderSerializer

class TopCoderViewSet(viewsets.ModelViewSet):
    queryset = TopCoder.objects.all()
    serializer_class = TopCoderSerializer

class CodeForcesGymViewSet(viewsets.ModelViewSet):
    queryset = CodeForcesGym.objects.all()
    serializer_class = CodeForcesGymSerializer

class GeekforgeeksViewSet(viewsets.ModelViewSet):
    queryset = Geekforgeeks.objects.all()
    serializer_class = GeekforgeeksSerializer

class CodingNinjasViewSet(viewsets.ModelViewSet):
    queryset = CodingNinjas.objects.all()
    serializer_class = CodingNinjasSerializer