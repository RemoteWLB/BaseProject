import jwt
import datetime

from rest_framework import authentication
from rest_framework import exceptions

from jwt import InvalidSignatureError

from remote.params import JWT_SALT, JWT_ALGO
from user.models import User
from utils.self_rest_framework.exceptions import AuthenticationExpired

DEFAULT_EXPIRE_TIME = datetime.timedelta(days=7)
DEFAULT_REFRESH_TIME = datetime.timedelta(days=30)


def get_default_expire_time():
    expire_time = datetime.datetime.now() + DEFAULT_EXPIRE_TIME
    return expire_time.timestamp()


def get_default_refresh_time():
    refresh_time = datetime.datetime.now() + DEFAULT_REFRESH_TIME
    return refresh_time.timestamp()


def get_default_payload():
    DEFAULT_PAYLOAD = {
        "expire_time": get_default_expire_time(),
        "refresh_time": get_default_refresh_time(),
        "origin": 1,
    }
    return DEFAULT_PAYLOAD


def create_token(payload, secret=JWT_SALT, algo=JWT_ALGO):
    return jwt.encode(payload, secret, algo)


def create_user_token(user_info):
    payload = get_default_payload()
    payload["user_info"] = user_info
    return create_token(payload)


def ValidJWToken(token, secret=JWT_SALT, algo=JWT_ALGO):
    try:
        if token in ["", "undefined"]:
            raise exceptions.AuthenticationFailed()
        payload = jwt.decode(token, secret, algo)
        expire_time = datetime.datetime.fromtimestamp(payload["expire_time"])
        if expire_time < datetime.datetime.now():
            raise AuthenticationExpired()
        return payload
    except InvalidSignatureError:
        raise exceptions.AuthenticationFailed()
    except Exception as e:
        print(e)
        raise e


class SelfAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN')
        if not token:
            raise exceptions.NotAuthenticated()
        try:
            payload = ValidJWToken(token)
            user = User.objects.get(uuid=payload['user_info']['user_id'])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed()
        return user, None


class SelfAuthenticationNoRequire(SelfAuthentication):
    def authenticate(self, request):
        try:
            return super().authenticate(request)
        except (exceptions.AuthenticationFailed, exceptions.NotAuthenticated, AuthenticationExpired):
            return None, None
