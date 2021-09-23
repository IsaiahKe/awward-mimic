from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import AppVote

class AppVoteApi(serializers.ModelSerializer):
    class Meta:
        model=AppVote
        fields=('appname','appimage','author','livelink','usability','content','design','total')