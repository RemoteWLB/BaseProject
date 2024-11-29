from rest_framework import status, exceptions
from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _
from utils.response import UnAuthResponse


def self_exception_handler(exc, context):
    if isinstance(exc, (exceptions.AuthenticationFailed, exceptions.NotAuthenticated, AuthenticationExpired)):
        return UnAuthResponse(0, exc.detail, {}, 0)


class AuthenticationExpired(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Token expired.')
    default_code = 'authentication_failed'
