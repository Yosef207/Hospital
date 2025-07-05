from rest_framework import serializers
from .models import Patient
class PatientSerializer(serializers.ModelSerializer):
    insurance_company = InsuranceCompanySerializer()
    class Meta:
        model = Patient
        fields = ['patient_id', 'name', 'birth_date', 'phone_number', 'insurance_company']
