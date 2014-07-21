from django.db import models

# Create your models here.
class RequestJob(models.Model):
    status = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True, editable=False)
    lastModified = models.DateTimeField(auto_now=True)
    result = models.ForeignKey(RequestResult, null=True, unique=True, default=None)
    completed = models.FloatField()

    class Meta:
        db_table = u'requestjob'
        app_label = u'operons.rest'

class RequestResult(models.Model):
    dateCreated = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = u'requestresult'
        app_label = u'operons.rest'
