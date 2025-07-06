# views.py
from rest_framework import generics
from .models import InsuranceCompany
from .serializers import InsuranceCompanySerializer

class InsuranceCompanyListCreate(generics.ListCreateAPIView):
    queryset = InsuranceCompany.objects.all()
    serializer_class = InsuranceCompanySerializer

class InsuranceCompanyDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = InsuranceCompany.objects.all()
   serializer_class = InsuranceCompanySerializer
