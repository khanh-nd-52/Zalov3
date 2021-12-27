from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response

from .renderers import UserRenderer
from .serializers import RegisterUserSerializer


class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = (permissions.AllowAny,)
    # def post(self, request):
    #     serializer = RegisterUserSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     content = {'code': '1000', 'message': 'OK',
    #                'data': serializer.data}
    #     return Response(content)
    renderer_classes = (UserRenderer,)
