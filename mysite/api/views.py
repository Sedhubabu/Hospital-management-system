from rest_framework import viewsets
from .serializers import DoctorDetailSerializer
from .models import DoctorDetail

class DoctorListViewSet(viewsets.ModelViewSet):
    queryset = DoctorDetail.objects.all()
    serializer_class = DoctorDetailSerializer
    