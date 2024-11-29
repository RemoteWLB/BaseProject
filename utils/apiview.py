from rest_framework.generics import ListAPIView, RetrieveAPIView

from utils.jwt import SelfAuthentication, SelfAuthenticationNoRequire
from utils.pagination import SelfPageNumberPagination


class SelfListAPIView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    def get_total(self):
        return self.paginator.page.paginator.count

    def params(self):
        if self.request.method == "GET":
            return self.request.GET.dict()
        else:
            return self.request.query_params

    pagination_class = SelfPageNumberPagination
    total = get_total


class SelfBaseAPIView(RetrieveAPIView):
    authentication_classes = []
    permission_classes = []

    def params(self):
        if self.request.method == "GET":
            return self.request.GET.dict()
        else:
            return {}


class AuthAPIView(SelfBaseAPIView):
    authentication_classes = (SelfAuthentication,)
    permission_classes = []


class AuthNoRequireAPIView(SelfBaseAPIView):
    authentication_classes = (SelfAuthenticationNoRequire,)
    permission_classes = []