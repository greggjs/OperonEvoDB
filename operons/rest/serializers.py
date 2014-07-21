from models import RequestJob
from rest_framework import serializers

class RequestJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestJob
        fields = ('id', 'status', 'dateCreated', 'lastModified', 'result', 'completed')

class RequestJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestResult
        fields = ('id', 'dateCreated')
