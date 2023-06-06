"""
URL configuration for companyapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api.views import *
from rest_framework import routers

router=routers.DefaultRouter()

router.register(r'codingplatforms',CodingPlatformViewSet)
router.register(r'allcontests',AllContestsViewSet)

router.register(r'leetcode',LeetcodeViewSet)
router.register(r'codechef',CodeChefViewSet)
router.register(r'codeforces',CodeforcesViewSet)

router.register(r'hackerrank',HackerRankViewSet)
router.register(r'hackerearth',HackerEarthViewSet)
router.register(r'csacademy',CSAcademyViewSet)
router.register(r'atcoder',AtCoderViewSet)
router.register(r'topcoder',TopCoderViewSet)
router.register(r'codeforcesgym',CodeForcesGymViewSet)
router.register(r'geekforgeeks',GeekforgeeksViewSet)
router.register(r'codingninjas',CodingNinjasViewSet)





urlpatterns = [
    path('',include(router.urls))
]
