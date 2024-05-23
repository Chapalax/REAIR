from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from reModule.reService.re_exec import get_domain
from reModule.reService.re_exec import get_nickname
from .serializers import TextSerializer, ValidationErrorSerializer, PaginationSerializer


# Create your views here.

class EmailExtractionViewSet(ViewSet):
    nicknames = []
    domains = []

    def post_emails_nickname(self, request):
        line = TextSerializer(data=request.data)
        if not line.is_valid():
            return Response(
                data=ValidationErrorSerializer({"errors": line.errors}).data,
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
                data=ValidationErrorSerializer({"errors": line.errors}).data,
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        result = get_domain(**line.validated_data)
        self.domains.append(result)
        return Response(
            data={"domain": result},
            status=status.HTTP_200_OK
        )

    def get_emails_nickname(self, request):
        serializer = PaginationSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(
                data=ValidationErrorSerializer({"errors": serializer.errors}).data,
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        first_index = (serializer.validated_data["page"] - 1) * 5
        second_index = serializer.validated_data["page"] * 5

        total = len(self.nicknames)
        if first_index >= total:
            return Response(
                data={"detail": "Page not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        result = self.nicknames[first_index: min(total, second_index)]
        amount = len(result)
        return Response(
            data={
                "nicknames": result,
                "amount": amount,
                "total": total
            },
            status=status.HTTP_200_OK
        )

    def get_emails_domain(self, request):
        serializer = PaginationSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(
                data=ValidationErrorSerializer({"errors": serializer.errors}).data,
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        first_index = (serializer.validated_data["page"] - 1) * 5
        second_index = serializer.validated_data["page"] * 5

        total = len(self.domains)
        if first_index >= total:
            return Response(
                data={"detail": "Page not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        result = self.domains[first_index: min(total, second_index)]
        amount = len(result)
        return Response(
            data={
                "domains": result,
                "amount": amount,
                "total": total
            },
            status=status.HTTP_200_OK
        )
