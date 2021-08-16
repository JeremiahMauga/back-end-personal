from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken
from .models import Inventory
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.serializers import *
from core.models import *

## The core of this functionality is the api_view decorator, which takes a list of HTTP methods that your view should respond to.
@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

# class InventoryViewSet(viewsets.ModelViewSet):
#     serializer_class = InventorySerializer
#     queryset = Inventory.objects.all()

class InventoryViewSet(ModelViewSet):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    def get_queryset(self):
        return Inventory.objects.filter(user=self.request.user)

class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST','GET','PUT','DELETE'])
def Inventory_Api(request):
    if (request.method == 'GET'):
        inv = Inventory.objects.all()
        serializer = InventorySerializer(inv,many=True)
        return Response(serializer.data)
    if(request.method == 'POST'):
        data = request.data
        serializer = InventorySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            res = {'msge':'Data has been created successfully'}
            return Response(res)
        return Response({'msg':serializer.errors})

# @api_view(['POST','GET'])
# def GetSummoner(request):  
#     print('request method is:', request.method)
#     print('request body is:', json.loads(request.body))
#     summonerName = json.loads(request.body)
#     print(summonerName['name'])
#     riot_api = (f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName['name']}?api_key=RGAPI-4acf0345-6759-4596-b5c3-42d6becafc52")
#     print(riot_api)
#     if (request.method == 'GET'):
#         inv = Inventory.objects.all()
#         serializer = RiotSerializer(inv,many=True)
#         print(serializer)
#         return Response(serializer.data)
#     response = (requests.get(riot_api)).json()
#     return Response(response)


# @api_view(['POST'])
# def GetSummonerAPIRequest(request):
#     tp_api = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Cornarian?api_key=RGAPI-55af0184-2264-483c-92e7-fd1ace2c61e1"
#     response = requests.get(tp_api)
#     return Response(data=response.json())

# class RiotView(APIView):
#     def post(self, request, *args, **kwargs):
#         my_result=GetSummoner(request.data.get('Cornarian'))
#         return Response(data={"my_return_data":my_result})


