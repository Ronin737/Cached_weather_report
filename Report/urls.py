from django.urls import path
from .views import HomeViewAPI, ReportAPI

urlpattern=[path("metar/<str:data>/",ReportAPI.as_view(),name='cached-view'),
            path("metar/<str:data>/<int:nocache>/",ReportAPI.as_view(),name='live-view'),
            path('',HomeViewAPI.as_view(),name='home-view'),
            path('metar/',HomeViewAPI.as_view(),name='home-view')]