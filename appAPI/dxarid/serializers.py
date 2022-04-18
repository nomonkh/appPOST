from rest_framework import serializers
from dxarid.models import *


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ('__all__')