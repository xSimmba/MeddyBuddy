from django.shortcuts import get_object_or_404
from .models import Medication
from .forms import FormAddMedication, FormEditMedication
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


class AddMedication(CreateView):
    """
    View to handle the addition of new medication.
    This view extends Django's CreateView to provide functionality for adding new medication entries.
    It uses the Medication model and the FormAddMedication form class.
    Methods:
        get_form_kwargs(self):
            Adds the request object to the form kwargs if the user is authenticated.
        form_valid(self, form):
            Sets the created_by field of the form instance to the current user before saving.
        get_success_url(self):
            Returns the URL to redirect to after a successful form submission.
    """

    model = Medication
    form_class = FormAddMedication
    template_name = "medication/medication_add.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.is_authenticated:
            kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("medication:home")



class MedicationListView(ListView):
    """
    A view that displays a list of medications for the current user.

    Attributes:
        model (Model): The model that this view will display.
        template_name (str): The path to the template that will render the view.
        context_object_name (str): The name of the context variable that will contain the list of medications.

    Methods:
        get_queryset(): Returns a queryset of medications filtered by the current user.
    """

    model = Medication
    template_name = "home.html"
    context_object_name = "medications"

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)


class DeleteMedication(DeleteView):
    """
    View to handle the deletion of a Medication instance.

    Attributes:
        model (Medication): The model that this view will act upon.
        template_name (str): The template to render for the delete confirmation page.
        success_url (str): The URL to redirect to upon successful deletion.

    Methods:
        get_object(queryset=None):
            Retrieves the Medication instance to be deleted. Ensures that the
            instance belongs to the current user. Raises Http404 if the user
            does not own the instance.
    """

    model = Medication
    template_name = "medication/medication_delete.html"
    success_url = reverse_lazy("medication:home")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.user == self.request.user:
            raise Http404
        return obj


class EditMedication(UpdateView):
    """
    View to handle the editing of a Medication instance.

    Attributes:
        model (Medication): The model that this view will interact with.
        form_class (FormEditMedication): The form class used to edit the Medication instance.
        template_name (str): The template used to render the edit form.
        success_url (str): The URL to redirect to upon successful form submission.

    Methods:
        get_object(self):
            Retrieves the Medication instance to be edited, ensuring it belongs to the current user.

        get_success_url(self):
            Returns the URL to redirect to upon successful form submission.
    """

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
    """
    Detail view for displaying a single Medication instance.

    Attributes:
        model (Medication): The model that this view will display.
        template_name (str): The template used to render the detail view.
        context_object_name (str): The context variable name to use for the object.

    Methods:
        get_queryset(self):
            Returns a queryset of Medication objects filtered by the current user.
    """

    model = Medication
    template_name = "medication/medication_detail.html"
    context_object_name = "medication"

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)
