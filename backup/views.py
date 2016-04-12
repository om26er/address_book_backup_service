from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

from backup.serializers import ContactSerializer


class AddContactView(CreateAPIView):

    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        if len(request.data) == 0:
            data = {'message': 'At least one parameter is necessary'}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)
