from django.urls import path
from .views import ReceptionistListCreateView, ReceptionistDetailView

urlpatterns = [
    path('receptionists/', ReceptionistListCreateView.as_view(), name='receptionist-list-create'),
    path('receptionists/<int:pk>/', ReceptionistDetailView.as_view(), name='receptionist-detail'),
]