from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .form import UploadForm


class UploadFormView(generic.FormView):
    template_name = 'upload/upload_form.html'
    form_class = UploadForm
    success_url = 'polls/'

    def form_valid(self, form):
        form.save()
        return HttpResponse('http://127.0.0.1:8000/polls')

# Create your views here.
