from django import forms
from .models import Medication

class FormAddMedication(forms.ModelForm):
    """
    FormAddMedication is a ModelForm for adding a new Medication instance.
    Attributes:
        Meta:
            model (Model): The model that this form is associated with.
            fields (list): The fields to include in the form.
    Methods:
        __init__(self, *args, **kwargs):
            Initializes the form, setting the 'user' field to the current user and hiding it.
        get_form_kwargs(self):
            Returns the keyword arguments for instantiating the form, including the request object.
    """
    class Meta:
        model = Medication
        fields = ['name', 'dosage', 'instructions', 'user']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['user'].initial = self.request.user
        self.fields['user'].widget = forms.HiddenInput()
        
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class FormEditMedication(forms.ModelForm):
    """
    FormEditMedication is a ModelForm for editing Medication instances.

    This form includes the following fields:
    - name: The name of the medication.
    - dosage: The dosage of the medication.
    - instructions: Instructions for taking the medication, displayed as a textarea with 4 rows.

    Meta:
        model: The model associated with this form is Medication.
        fields: Specifies the fields to be included in the form.
        widgets: Customizes the widget for the 'instructions' field to be a textarea with 4 rows.
    """
    class Meta:
        model = Medication
        fields = ("name", "dosage", "instructions")
        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 4}),  
        }
