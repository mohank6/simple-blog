from rest_framework import status
from rest_framework.response import Response

from app.api import api


class ResponseBuilder:

    def __init__(self):
        self.results = {}
        self.errors = {}
        '''
            Binary(1 or -1), later changes to code based on api.py (eg: 400)
            Sent with reponse in body(JSON format)
        '''
        self.status_code = 1
        self.status_message = ""
        self.status = status.HTTP_200_OK

    def success(self):
        self.status_code = 1
        return self

    def fail(self):
        self.status_code = -1
        return self

    def ok_200(self):
        self.status = status.HTTP_200_OK
        return self

    def created_201(self):
        self.status = status.HTTP_201_CREATED
        return self

    def accepted_202(self):
        self.status = status.HTTP_202_ACCEPTED
        return self

    def not_found_404(self):
        self.status = status.HTTP_404_NOT_FOUND
        return self

    def bad_request_400(self):
        self.status = status.HTTP_400_BAD_REQUEST
        return self

    def user_unauthorized_401(self):
        self.status = status.HTTP_401_UNAUTHORIZED
        return self

    def user_forbidden_403(self):
        self.status = status.HTTP_403_FORBIDDEN
        return self

    # Set status code based on api.py
    def set_status_code(self, status_code):
        self.status_code = status_code
        return self

    def message(self, status_message):
        self.status_message = status_message
        return self

    def result_object(self, result):
        self.results = result
        return self

    def error_object(self, errors):
        self.errors = errors
        return self

    def get_response(self):
        content = self.get_json()
        return Response(content, status=self.status)

    def get_json(self):
        status_message = self.status_message
        if not self.status_code == 1:
            status_message = api.error_messages[self.status_code]

        return dict(
            status_code=self.status_code,
            status_message=status_message,
            data=self.results,
            error=self.errors,
        )

    '''
        Set succes or fail -> Http status -> Custom status code based on api.py(optional)
        -> Result or Error (optional) -> Message(optional) -> Get Response
    '''

    def get_200_success_response(self, message, result):
        return (
            self.success()
            .ok_200()
            .result_object(result)
            .message(message)
            .get_response()
        )

    def get_200_fail_response(self, error_code):
        return self.fail().ok_200().set_status_code(error_code).get_response()

    def get_201_success_response(self, message, result):
        return (
            self.success()
            .created_201()
            .result_object(result)
            .message(message)
            .get_response()
        )

    def get_400_bad_request_response(self, error_code, errors):
        return (
            self.fail()
            .bad_request_400()
            .set_status_code(error_code)
            .error_object(errors)
            .get_response()
        )

    def get_404_not_found_response(self, error_code):
        return self.fail().not_found_404().set_status_code(error_code).get_response()

    def get_401_user_unauthorized(self, error_code):
        return (
            self.fail()
            .user_unauthorized_401()
            .set_status_code(error_code)
            .get_response()
        )
