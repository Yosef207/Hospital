from django.urls import path
from .views import InsuranceCompanyListCreate, InsuranceCompanyDetail

urlpatterns = [
 path('insurance-companies/', InsuranceCompanyListCreate.as_view(), name='insurance-company-list-create'),
 path('insurance-companies/<int:pk>/', InsuranceCompanyDetail.as_view(), name='insurance-company-detail'),
]