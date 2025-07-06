from django.urls import path
from .views import MedicationListCreateView, MedicationDetailView

urlpatterns = [
    path('medications/', MedicationListCreateView.as_view(), name='medication-list-create'),
    path('medications/<int:pk>/', MedicationDetailView.as_view(), name='medication-detail'),
]
