from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics, permissions, serializers

from buysell.models import SmsStats, Profile, User
from buysell.serializers import  ProfileSerializer, UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
import requests
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated  # <-- Here

# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.contrib.auth.models import Group
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django.contrib.auth import get_user_model  # If used custom user model
from rest_framework.generics import CreateAPIView


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    try:
        userobj = get_user_model().objects.get(username=username)
    except SmsStats.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    return Response({'token': token.key, 'email': userobj.email},
                    status=HTTP_200_OK)


# register user
class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer



@api_view(['GET'])
def getWazirxData(request):
    url = 'https://api.wazirx.com/api/v2/tickers'
    if request.method == 'GET':
        response = requests.get(url)
        return JsonResponse(response.json(),status=status.HTTP_200_OK, safe=True)


@api_view(['GET'])
def getHistoricalData(request):
    id = request.query_params.get('id')

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    if request.method == 'GET':
        headers = {"X-CMC_PRO_API_KEY": "b6f39c3c-2d63-4660-8d6a-2a9b01014a4a"}
        params = {"id": id}
        response = requests.get(url, params=params, headers=headers)

        return JsonResponse(response.json(), safe=False)




@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def profile(request):
    if request.method == 'GET':
        # tutorials = Profile.objects.all()
        email = request.query_params.get('email')
        # print('===============================', email)
        try:
            data = Profile.objects.get(email=email)
            data_serializer = ProfileSerializer(data)
            return JsonResponse(data_serializer.data)
        except:
            return JsonResponse({'message': 'The email does not exist'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        post_data = JSONParser().parse(request)
        profile_serializer = ProfileSerializer(data=post_data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return JsonResponse(profile_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'PUT':
        email = request.data.get('email')
        try:
            data_obj = Profile.objects.get(email=email)

            # put_data = JSONParser().parse(request)
            # jsonData = put_data['currentState']
            tutorial_serializer = ProfileSerializer(data_obj, data=request.data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()

                return JsonResponse(tutorial_serializer.data)

            return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse({'message': 'The email does not exist'}, status=status.HTTP_404_NOT_FOUND)


