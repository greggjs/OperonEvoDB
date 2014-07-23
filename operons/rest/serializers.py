from models import Job, Result, Figure
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'status', 'dateCreated', 'lastModified', 'result', 'completed')

class ResultSerializer:
    def __init__(self, result, many=False):
        self.data = SecretResultSerializer(result, many=many).data
        if not many:
            figures = Figure.objects.filter(result__exact=result)
            self.data['figures'] = FigureSerializer(figures, many=True).data
        else:
            for index, result in enumerate(self.data):
                figures = Figure.objects.filter(result__exact=result['id'])
                result['figures'] = FigureSerializer(figures, many=True).data
                self.data[index] = result

class SecretResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'deletions', 'duplications', 'splits', 'rearrangements', 'hgt', 'dateCreated')

class FigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Figure
        fields = ('id', 'url')
