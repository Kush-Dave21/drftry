from wsgiref.validate import validator
from rest_framework import serializers
from appmate.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['name']