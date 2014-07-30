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
from Bio import SeqIO
from StringIO import StringIO

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
    query = forms.CharField(required=True)

    def clean_query(self):
        try:
            # check to see if it is valid json and thus a list of genes
            gene_list = json.loads(self.cleaned_data['query'])
            if not isinstance(gene_list, list):
                raise ValidationError("Requires a list of gene names be sent")
            return {
                'type' : 'GENE_LIST',
                'data' : gene_list
            }
        except ValueError:
            # check to make sure the input is a valid sequence
            io = StringIO(self.cleaned_data['query'])
            sequences = list(SeqIO.parse(open(io), 'fasta'))
            if not sequences:
                raise ValidationError("The query as a sequence must be in valid FASTA format")
            return {
                'type' : 'FASTA',
                'data' : sequences
            }

    def submit(self, request):
        job = Job(query=json.dumps(self.cleaned_data['query']))

        try:
            job.save()
        except DatabaseError:
            raise DatabaseIntegrityError()

        if self.cleaned_data['query']['type'] == 'FASTA':

        else:




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
