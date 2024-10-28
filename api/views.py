from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

class ExampleViewSet(ViewSet):
    @action(detail=False, methods=['get'])
    def example(self, request):
        return Response({"message": "Hello, World!"})
