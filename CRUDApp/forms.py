from django import forms
from . import models


class EmpForms(forms.ModelForm):
    class Meta:
        model = models.EmpModel
        fields = "__all__"
