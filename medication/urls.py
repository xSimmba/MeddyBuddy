from django.urls import path
from views import AddMedication

urlspatterns = [
    path('add/medication' , AddMedication.as_view() , name="add_meds")
]