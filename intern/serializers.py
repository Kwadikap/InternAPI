from dataclasses import fields
from .models import Intern
from rest_framework import serializers

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = ['id', 'name', 'college', 'year', 'company']