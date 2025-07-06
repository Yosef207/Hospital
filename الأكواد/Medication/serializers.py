from rest_framework import serializers
from .models import Medication

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['medication_id', 'name', 'dosage']
