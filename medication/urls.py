from django.urls import path
from .views import AddMedication, DeleteMedication, MedicationListView , EditMedication, DetailMedication

urlpatterns = [
    path('add/', AddMedication.as_view(), name='add_medication'),
    path('delete/<int:pk>/', DeleteMedication.as_view(), name='delete_medication'),
    path('list/', MedicationListView.as_view(), name='medication_list'),
    path('edit/<int:pk>/', EditMedication.as_view() , name='edit_medication'),
    path('detail/<int:pk>/', DetailMedication.as_view() , name='medication_detail')
]