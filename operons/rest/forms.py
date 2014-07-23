'''
    This file holds all of the forms for the cleaning and validation of
    the parameters being used for for the Request Jobs & their Request Results
    used for searching.

    @created: July 16, 2014
    @author: Andrew Oberlin
'''
from django import forms
from models import Job
from serializers import JobSerializer, ResultSerializer
from exceptions import JobDoesNotExist
from django.core.exceptions import ValidationError
import json

class JobForm(forms.Form):
    # Path parameters
    request_job_id = forms.IntegerField(required=True)

    def clean_request_job_id(self):
        if self.cleaned_data['request_job_id'] < 0:
            raise ValidationError("The given Job's id is incorrect.")
        return self.cleaned_data['request_job_id']

    def submit(self, request):
        '''
            Returns a serialized job with its current status. Used for polling.
        '''
        try:
            job = Job.objects.get(pk__exact=self.cleaned_data['request_job_id'])
        except (Job.DoesNotExist, ValueError):
            raise JobDoesNotExist():

        return JobSerializer(job).data

class JobListForm(forms.Form):
    # Post parameters
    sequence = forms.CharField(required=True)

    def clean_sequence(self):
        try:
            # check to see if it is valid json and thus a list of genes

        except ValueError:
            # check to make sure the input is a valid sequence


    def submit(self, request):




class ResultForm(forms.Form):
    # Path parameters
    request_result_id = forms.IntegerField(required=True)

    def clean_request_result_id(self):
        if self.cleaned_data['request_result_id'] < 0:
            raise ValidationError("The given Result's id is incorrect.")
        return self.cleaned_data['request_result_id']

    def submit(self, request):
        '''
            Returns a serialized result corresponding to the given id.
        '''
        try:
            result = Result.objects.get(pk__exact=self.cleaned_data['request_result_id'])
        except (Job.DoesNotExist, ValueError):
            raise JobDoesNotExist():

        return ResultSerializer(result).data
