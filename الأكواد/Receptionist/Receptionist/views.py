from rest_framework import generics
from .models import Receptionist
from .serializers import ReceptionistSerializer

class ReceptionistListCreateView(generics.ListCreateAPIView):
    queryset = Receptionist.objects.all()
    serializer_class = ReceptionistSerializer

class ReceptionistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receptionist.objects.all()
    serializer_class = ReceptionistSerializer
