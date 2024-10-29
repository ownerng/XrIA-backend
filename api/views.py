from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

@extend_schema(summary=("Registrar un nuevo Usuario"),
        description=("Registrar un nuevo Usuario"),
        tags=['Example'])
class ExampleViewSet(ViewSet):
    @action(detail=False, methods=['get'])
    def example(self, request):
        return Response({"message": "Hello, World!"})
