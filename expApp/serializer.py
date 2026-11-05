from rest_framework import serializers
from expApp.models import expModel
from django.contrib.auth.models import User

class ExpSerializer(serializers.ModelSerializer):
    class Meta:
        model=expModel
        read_only_fields = ["owner"]
        fields="__all__"

