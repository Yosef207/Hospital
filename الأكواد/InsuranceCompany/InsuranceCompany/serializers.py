from rest_framework import serializers
from .models import InsuranceCompany

class InsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceCompany
        fields = ['insurance_id', 'coverage_type', 'contact_info', 'name']