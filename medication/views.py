from django.shortcuts import get_object_or_404
from .models import Medication
from .forms import FormAddMedication, FormEditMedication
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponseRedirect



def home(request):
    return render(request, "home.html")


class AddMedication(CreateView):

    model = Medication
    form_class = FormAddMedication
    template_name = "medication/medication_add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("medication:home")



class MedicationListView(ListView):
    template_name = "home.html"
    context_object_name = "medications"

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)


class DeleteMedication(DeleteView):
    model = Medication
    template_name = "medication/medication_delete.html"
    success_url = reverse_lazy("medication:home")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.user == self.request.user:
            raise Http404
        return obj


class EditMedication(UpdateView):
    model = Medication
    form_class = FormEditMedication
    template_name = "medication/medication_edit.html"
    sucess_url = reverse_lazy("medication_list")

    def get_object(self):
        medication_id = self.kwargs.get("pk")
        return get_object_or_404(
            Medication, id=medication_id, user_id=self.request.user.id
        )

    def get_success_url(self):
        return reverse("medication:home")


class DetailMedication(DetailView):
    model = Medication
    template_name = "medication/medication_detail.html"
    context_object_name = "medication"

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)
