from rest_framework.views import APIView
from rest_framework.response import Response
from exceptions import BadRequestException

from forms import JobForm, JobListForm, ResultForm


# Create your views here.
class ResultAPI(APIView):
    '''
       Class for rendering the view for getting a Request's result.
    '''

    def get(self, request, request_result_id):
        '''
            Method for getting a Result based on the id provided.
        '''
        params = dict((key, val) for key, val in request.QUERY_PARAMS.iteritems())
        params['request_result_id'] = request_result_id
        form = ResultForm(params)

        if not form.is_valid():
            raise BadRequestException()

        return Response(form.submit(request))


class JobListAPI(APIView):
    '''
       Class for rendering the view for getting a Request's result.
    '''

    def post(self, request):
        '''
            Method for getting a Result based on the id provided.
        '''
        params = dict((key, val) for key, val in request.DATA.iteritems())
        params.update(request.QUERY_PARAMS)
        form = JobListForm(params)

        if not form.is_valid():
            raise BadRequestException()

        return Response(form.submit(request))

class JobAPI(APIView):
    '''
       Class for rendering the view for getting a Request's job status.
    '''

    def get(self, request, request_job_id):
        '''
            Method for getting a Job based on the id provided.
        '''
        params = dict((key, val) for key, val in request.QUERY_PARAMS.iteritems())
        params['request_job_id'] = request_job_id
        form = JobForm(params)

        if not form.is_valid():
            raise BadRequestException()

        return Response(form.submit(request))
