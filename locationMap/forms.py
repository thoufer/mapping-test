from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from mapwidgets.widgets import GooglePointFieldWidget
from .models import Observation

class ObservationAdmin(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ("obsdate", "count", "location")
        widgets = {
           "location": GooglePointFieldWidget,
           "obsdate": forms.DateInput(attrs={'class': 'datepicker'})
           }

class ObservationAddForm(forms.ModelForm):

  class Meta:
    model = Observation
    fields = ("obsdate", "count", "location")
    widgets = {
        "location": GooglePointFieldWidget,
        }

class ObsAddForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Observation
        fields = ("obsdate", "count", "location")
        widgets = {
            "location": GooglePointFieldWidget,
            }
