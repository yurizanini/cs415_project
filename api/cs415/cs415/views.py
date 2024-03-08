import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User, Order, Orderservices, Phonetype, Services, Useraddress, Userphone, Pagedata, Userinfo
from cs415.serializers import PhoneSerializerGet, UserinfoSerializer, AddressSerializerGet, PageDataSerializer, UserSerializer, OrderSerializer, OrderServicesSerializer, PhoneTypeSerializer, ServicesSerializer, UserAddressSerializer, UserPhoneSerializer
from cs415.settings import JWT_AUTH
from cs415.authentication import JWTAuthentication

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
    
class PageDataAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        serializer = PageDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        page_datas = Pagedata.objects.all()
        serializer = PageDataSerializer(page_datas, many=True)
        return Response({'pages': serializer.data})
    
    
class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({'success': False,
                             'error': 'Email and Password must have a value'},
                             status = status.HTTP_400_BAD_REQUEST)

        check_user = User.objects.filter(email=email).exists()
        if check_user == False:
            return Response({'success': False,
                             'error': 'User with this email does not exist'},
                             status=status.HTTP_404_NOT_FOUND)

        check_pass = User.objects.filter(email = email, pass_word=password).exists()
        if check_pass == False:
            return Response({'success': False,
                             'error': 'Incorrect password for user'},
                             status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(email = email, pass_word=password)

        # add last login to User table
        serializer = UserSerializer(user, data={'last_login': str(datetime.datetime.now())}, partial=True)
        if serializer.is_valid():
            serializer.save()

        if user is not None:
            jwt_token = JWTAuthentication.create_jwt(user)
            data = {
                'token': jwt_token
            }
            return Response({'success': True,
                             'user_id': user.user_id,
                             'token': jwt_token},
                             status=status.HTTP_200_OK)
        else:
            return Response({'success': False,
                             'error': 'Invalid Login Credentials'},
                             status=status.HTTP_400_BAD_REQUEST)
        
class GetSingleUserAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user_data = {}
        user = User.objects.get(pk=id)
        user_serial = UserSerializer(user)
        user_data.update({"user": user_serial.data})
        addresses = AddressSerializerGet(Useraddress.objects.filter(user=user), many=True)
        user_data.update({"addresses": addresses.data})
        info = UserinfoSerializer(Userinfo.objects.filter(user=user), many=True)
        # user_data.update({"info": info.data})
        phone = PhoneSerializerGet(Userphone.objects.filter(user=user).select_related(), many=True)
        user_data.update({"phones": phone.data})
        return Response(user_data)
    
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

class GetSinglePageDataAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        page = Pagedata.objects.get(pk=id)
        serializer = PageDataSerializer(page)
        return Response({'page': serializer.data})
    
class GetSingleUserInfoAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user = User.objects.get(pk=id)
        info = Userinfo.objects.filter(user=user)
        serializer = UserinfoSerializer(info, many=True)
        return Response({'info': serializer.data})
    
class UserInfoAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        serializer = UserinfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user_infos = Userinfo.objects.all()
        serializer = UserinfoSerializer(user_infos, many=True)
        return Response({'user_infos': serializer.data})