from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import AuthorizationValidateSerializer, RegistrationValidateSerializer, UserConfirmationSerializer
from rest_framework.authtoken.models import Token
from users.models import *
import random
import string


def generate_confirmation_code():
    return ''.join(random.choices(string.digits, k=6))


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegistrationValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User.objects.create_user(username=username, password=password, is_active=False)

        confirmation_code = generate_confirmation_code()
        UserProfile.objects.create(user=user, confirmation_code=confirmation_code)
        return Response(
            status=status.HTTP_201_CREATED,
            data={'user_id': user.id, 'activation_code': confirmation_code},
        )


class UserConfirmationAPIView(APIView):
    def post(self, request):
        serializer = UserConfirmationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        confirmation_code = serializer.validated_data.get('confirmation_code')

        try:
            user_profile = UserProfile.objects.get(confirmation_code=confirmation_code, is_confirmed=False)
        except UserProfile.DoesNotExist:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED, data={'message': 'Invalid confirmation code'}
            )

        user_profile.user.is_active = True
        user_profile.is_confirmed = True
        user_profile.user.save()
        user_profile.save()

        return Response(status=status.HTTP_200_OK, data={'message': 'User confirmed successfully'})


class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = AuthorizationValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token_, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token_.key})

        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'message': 'User not found'})

# @api_view(['POST'])
# def registration_api_view(request):
#     serializer = RegistrationValidateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     username = serializer.validated_data.get('username')
#     password = serializer.validated_data.get('password')
#
#     user = User.objects.create_user(username=username, password=password,
#                                     is_active=False)
#
#     confirmation_code = generate_confirmation_code()
#     UserProfile.objects.create(user=user, confirmation_code=confirmation_code)
#     return Response(status=201, data={'user_id': user.id, 'activation_code': confirmation_code})
#
#
# @api_view(['POST'])
# def user_confirmation_api_view(request):
#     serializer = UserConfirmationSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     confirmation_code = serializer.validated_data.get('confirmation_code')
#
#     try:
#         user_profile = UserProfile.objects.get(confirmation_code=confirmation_code, is_confirmed=False)
#     except UserProfile.DoesNotExist:
#         return Response(status=401, data={'message': 'Invalid confirmation code'})
#
#     user_profile.user.is_active = True
#     user_profile.is_confirmed = True
#     user_profile.user.save()
#     user_profile.save()
#
#     return Response(status=200, data={'message': 'User confirmed successfully'})
#
#
# @api_view(['POST'])
# def authorization_api_view(request):
#     serializer = AuthorizationValidateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     username = serializer.validated_data.get('username')
#     password = serializer.validated_data.get('password')
#
#     user = authenticate(username=username, password=password)
#
#     if user is not None:
#         token_, created = Token.objects.get_or_create(user=user)
#         return Response(data={'key': token_.key})
#
#     return Response(status=401, data={'message': 'User not found'})
