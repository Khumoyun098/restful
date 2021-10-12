from django.contrib.auth import login
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import CarSerializer, LoginSerializer
from dev.models import Car


class CarViewSet(viewsets.ModelViewSet):
    """
    All cars with pagination
    """
    queryset = Car.objects.all().order_by('-created_time')
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]


class LoginView(generics.GenericAPIView):
    """
    Sample login for vue page
    """

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)

        return Response(
            {"token": "TokenNotAsignedYet",
             'user_id': user.id,
             'first_name': user.first_name or None,
             'last_name': user.last_name or None,
             'hello_msg': "Hello user"
             },
            status=status.HTTP_200_OK)