from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_302_FOUND, HTTP_401_UNAUTHORIZED


class SuccessResponse(Response):
    def __init__(self, result, msg, data=None, code=-1, status=HTTP_200_OK, template_name=None, headers=None,
                 exception=False, content_type=None):
        payload = {
            "result": result,
            "msg": msg,
            "data": data,
            "code": code
        }
        super().__init__(payload, status, template_name, headers, exception, content_type)


class FailResponse(Response):
    def __init__(self, result=0, msg=None, data=None, code=0, status=HTTP_400_BAD_REQUEST, template_name=None,
                 headers=None, exception=False, content_type=None):
        payload = {
            "result": result,
            "msg": msg,
            "data": data,
            "code": code
        }
        super().__init__(payload, status, template_name, headers, exception, content_type)


class UnAuthResponse(Response):
    def __init__(self, result=0, msg=None, data=None, code=0, status=HTTP_401_UNAUTHORIZED, template_name=None,
                 headers=None, exception=False, content_type=None):
        payload = {
            "result": result,
            "msg": msg,
            "data": data,
            "code": code
        }
        super().__init__(payload, status, template_name, headers, exception, content_type)


def Redirect(url):
    return redirect(url)
