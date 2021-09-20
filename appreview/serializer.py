from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Profile

class Morara(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('','')