from rest_framework import viewsets

from .serializers import SpeciesSerializer
from .models import Species


# class PersonViewSet(viewsets.ModelViewSet):
#    queryset = Person.objects.all()
#    serializer_class = PersonSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
   queryset = Species.objects.all()
   serializer_class = SpeciesSerializer
