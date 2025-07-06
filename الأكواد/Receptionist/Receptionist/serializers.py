from rest_framework import serializers
from .models import Receptionist

class ReceptionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptionist
        fields = ['receptionist_id', 'joptitle', 'name', 'email', 'phone']
