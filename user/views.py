from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


from django.contrib.auth.models import User

from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserView(APIView):

    def get(self, request, *args, **kwargs):

        queryset = User.objects.all()
        user_serializer = UserSerializer(queryset, many=True)

        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def get(self, request, pk):

        queryset = User.objects.get(pk=pk)
        if not queryset:
            return Response(
                {"res": "User id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)