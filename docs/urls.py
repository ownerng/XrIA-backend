# docs/urls.py

from django.urls import path
from .views import PDFView

urlpatterns = [
    path('pdf/', PDFView.as_view(), name='pdf-view'),
]
