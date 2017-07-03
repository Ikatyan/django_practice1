from django import forms
from .models import UploadedFile


class UploadForm(forms.Form):
    name = forms.CharField(50)
    comment = forms.CharField(100)
    file = forms.FileField()


