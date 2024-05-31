from rest_framework import serializers
from .models import DoctorDetail


class  DoctorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDetail
        fields ='__all__'
