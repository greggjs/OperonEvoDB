'''
    This file holds all of the forms for the cleaning and validation of
    the parameters being used for for the Request Jobs & their Request Results
    used for searching.

    @created: July 16, 2014
    @author: Andrew Oberlin
'''
from django import forms
from models import RequestJob
from serializers import RequestJobSerializer, RequestResultSerializer
from exceptions import RequestJobDoesNotExist
from django.core.exceptions import ValidationError

class RequestJobForm(forms.Form):
    # Path parameters
    request_job_id = forms.IntegerField(required=True)

    def clean_request_job_id(self):
        if self.cleaned_data['request_job_id'] < 0:
            raise ValidationError("The given RequestJob's id is incorrect.")
        return self.cleaned_data['request_job_id']

    def submit(self, request):
        '''
            Returns a serialized job with its current status. Used for polling.
        '''
        try:
            job = RequestJob.objects.get(pk__exact=self.cleaned_data['request_job_id'])
        except (RequestJob.DoesNotExist, ValueError):
            raise RequestJobDoesNotExist():

        return RequestJobSerializer(job).data

class RequestJobListForm(forms.Form):
    pass

class RequestResultForm(forms.Form):
    # Path parameters
    request_result_id = forms.IntegerField(required=True)

    def clean_request_result_id(self):
        if self.cleaned_data['request_result_id'] < 0:
            raise ValidationError("The given RequestResult's id is incorrect.")
        return self.cleaned_data['request_result_id']

    def submit(self, request):
        '''
            Returns a serialized result corresponding to the given id.
        '''
        try:
            result = RequestResult.objects.get(pk__exact=self.cleaned_data['request_result_id'])
        except (RequestJob.DoesNotExist, ValueError):
            raise RequestJobDoesNotExist():

        return RequestResultSerializer(result).data
