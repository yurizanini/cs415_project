from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User, Order, Orderservices, Phonetype, Services, Useraddress, Userphone
from cs415.serializers import UserSerializer, OrderSerializer, OrderServicesSerializer, PhoneTypeSerializer, ServicesSerializer, UserAddressSerializer, UserPhoneSerializer

class UserAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetSingleUserAPIView(APIView):
    def get(self,request,id):
        users = User.objects.get(pk=id)
        serializer = UserSerializer(users)
        return Response({'users': serializer.data})
    
class OrderAPIView(APIView):
    def get(self,request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({'orders': serializer.data})
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetSingleOrderAPIView(APIView):
    def get(self,request,id):
        orders = Order.objects.get(pk=id)
        serializer = OrderSerializer(orders)
        return Response({'orders': serializer.data})
    
class OrderServicesAPIView(APIView):
    def get(self,request):
        orderservices = Orderservices.objects.all()
        serializer = OrderServicesSerializer(orderservices, many=True)
        return Response({'orderservices': serializer.data})
    def post(self, request):
        serializer = OrderServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PhonetypeAPIView(APIView):
    def get(self,request):
        phonetype = Phonetype.objects.all()
        serializer = PhoneTypeSerializer(phonetype, many=True)
        return Response({'phonetype': serializer.data})
    def post(self, request):
        serializer = PhoneTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ServicesAPIView(APIView):
    def get(self,request):
        services = Services.objects.all()
        serializer = ServicesSerializer(services, many=True)
        return Response({'services': serializer.data})
    def post(self, request):
        serializer = ServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UseraddressAPIView(APIView):
    def get(self,request):
        useraddress = Useraddress.objects.all()
        serializer = UserAddressSerializer(useraddress, many=True)
        return Response({'useraddress': serializer.data})
    def post(self, request):
        serializer = UserAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserphoneAPIView(APIView):
    def get(self,request):
        userphone = Userphone.objects.all()
        serializer = UserPhoneSerializer(userphone, many=True)
        return Response({'userphone': serializer.data})
    def post(self, request):
        serializer = UserPhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
