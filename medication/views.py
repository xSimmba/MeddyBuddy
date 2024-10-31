from django.shortcuts import render
from models import Medication
from forms import FormAddMedication
from django.utils import timesince
from django.urls import reverse
# Create your views here.



class AddMedication():
    model = Medication
    form_class = FormAddMedication
    template_name = 'templates/medicationForm.html'


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.is_authenticated:
            kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('')
     