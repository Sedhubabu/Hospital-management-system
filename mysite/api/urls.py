
from django.urls import path, include
from rest_framework import routers

from .views import DoctorListViewSet

router =routers.DefaultRouter()
router.register('DoctorList', DoctorListViewSet, basename='DoctorList')

urlpatterns = [
    path('', include(router.urls)),
]