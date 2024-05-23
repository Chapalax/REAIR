from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from reModule.reService.re_exec import get_domain
from reModule.reService.re_exec import get_nickname
from .serializers import TextSerializer


# Create your views here.

class EmailExtractionViewSet(ViewSet):

    nicknames = []
    domains = []

    def post_emails_nickname(self, request):
        line = TextSerializer(data=request.data)
        if not line.is_valid():
            return Response(
                data=line.errors,
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        result = get_nickname(**line.validated_data)
        self.nicknames.append(result)
        return Response(
            data={"nickname": result},
            status=status.HTTP_200_OK
        )

    def post_emails_domain(self, request):
        line = TextSerializer(data=request.data)
        if not line.is_valid():
            return Response(
                data=line.errors,
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        result = get_domain(**line.validated_data)
        self.domains.append(result)
        return Response(
            data={"domain": result},
            status=status.HTTP_200_OK
        )

    def get_emails_nickname(self, _):
        total = len(self.nicknames)
        print(total)
        return Response(
            data={
                "nicknames": self.nicknames,
                "total": total
            },
            status=status.HTTP_200_OK
        )

    def get_emails_domain(self, _):
        total = len(self.domains)
        return Response(
            data={
                "domains": self.domains,
                "total": total
            },
            status=status.HTTP_200_OK
        )
