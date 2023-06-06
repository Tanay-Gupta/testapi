from django.shortcuts import render,HttpResponse
from rest_framework import viewsets

from api.models import Leetcode,CodeChef
from api.serializers import CodeChefSerializer,LeetcodeSerializer


class LeetcodeViewSet(viewsets.ModelViewSet):
    queryset=Leetcode.objects.all()
    serializer_class=LeetcodeSerializer 

class CodeChefViewSet(viewsets.ModelViewSet):
    queryset=CodeChef.objects.all()
    serializer_class=CodeChefSerializer     