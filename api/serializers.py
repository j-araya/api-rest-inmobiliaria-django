from rest_framework import serializers

from properties.models import Property


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
