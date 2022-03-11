from rest_framework import serializers
#from django.contrib.auth.models import User

from .models import Species


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('id','first', 'parent_n')

    def to_representation(self, instance):
        self.fields['parent_n'] = SpeciesSerializer(read_only=True)
        return super(SpeciesSerializer, self).to_representation(instance)


