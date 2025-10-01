from rest_framework import serializers

from cities.models import Address

class AddressPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('street_name', 'number', 'neighborhood')