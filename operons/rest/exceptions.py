from rest_framework.exceptions import APIException

class BadRequestException(APIException):
    '''
        Bad Request Exception.
    '''
    status_code = 400
    default_detail = "A Bad Request was made for the API. Revise input parameters."

class JobDoesNotExist(APIException):
    '''
        Job does not exist error.
    '''
    status_code = 404
    default_detail = "The request_job_id provided does not refer to a job in this database."
