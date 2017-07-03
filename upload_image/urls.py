from django.conf.urls import url
from .views import UploadFormView

app_name = 'upload'
urlpatterns = [
    url(r'^$', UploadFormView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
]
