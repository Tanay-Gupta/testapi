from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from api.services.leet_code_service import LeetCodeService
from api.models import Company,Employee,Leetcode
from api.serializers import CompanySerializer,EmployeeSerializer,LeetcodeSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer 


class LeetcodeViewSet(viewsets.ModelViewSet):
    Leetcode.objects.all().delete()
    LeetCodeService().update_contests()
    queryset=Leetcode.objects.all()
    serializer_class=LeetcodeSerializer 