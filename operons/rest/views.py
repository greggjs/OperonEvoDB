from rest_framework.views import APIView
from rest_framework.response import Response
from exceptions import BadRequestException

from forms import RequestJobForm, RequestJobListForm, RequestResultForm


# Create your views here.
class RequestResultAPI(APIView):
    '''
       Class for rendering the view for getting a Request's result.
    '''

    def get(self, request, request_result_id):
        '''
            Method for getting a RequestResult based on the id provided.
        '''
        params = dict((key, val) for key, val in request.QUERY_PARAMS.iteritems())
        params['request_result_id'] = request_result_id
        form = RequestResultForm(params)

        if not form.is_valid():
            raise BadRequestException()

        return Response(form.submit(request))


class RequestJobListAPI(APIView):
    '''
       Class for rendering the view for getting a Request's result.
    '''

    def post(self, request):
        '''
            Method for getting a RequestResult based on the id provided.
        '''
        params = dict((key, val) for key, val in request.DATA.iteritems())
        params.update(request.QUERY_PARAMS)
        form = RequestJobListForm(params)

        if not form.is_valid():
            raise BadRequestException()

        return Response(form.submit(request))

class RequestJobAPI(APIView):
    '''
       Class for rendering the view for getting a Request's job status.
    '''

    def get(self, request, request_job_id):
        '''
            Method for getting a RequestJob based on the id provided.
        '''
        params = dict((key, val) for key, val in request.QUERY_PARAMS.iteritems())
        params['request_job_id'] = request_job_id
        form = RequestJobForm(params)

        if not form.is_valid():
            raise BadRequestException()

        return Response(form.submit(request))
