# docs/views.py

from django.http import FileResponse, Http404
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
import os

@extend_schema(
    tags=['docs'],
    description="Endpoint to download a pre-existing PDF document located at 'docs/doc/enviar.pdf'."
)
class PDFView(APIView):
    def get(self, request):
        file_path = os.path.join('docs', 'doc', 'doc.pdf')

        if not os.path.exists(file_path):
            raise Http404("PDF file not found.")

        # Abrir el archivo en modo lectura binaria
        response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="document.pdf"'
        return response
