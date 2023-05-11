from rest_framework import viewsets
# from rest_framework import permissions

from api.serializers import PropertySerializer
from properties.models import Property

class PropertyViewSet(viewsets.ModelViewSet):

    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    # permission_classes = [permissions.IsAuthenticated]