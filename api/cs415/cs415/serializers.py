from rest_framework import serializers
from cs415.models import User, Order, Orderservices, Phonetype, Services, Useraddress, Userphone, Pagedata, Addresstype

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields= '__all__'

class OrderServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderservices
        fields= '__all__'

class PhoneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonetype
        fields= '__all__'

class PhoneSerializerGet(serializers.ModelSerializer):
    phone_type = PhoneTypeSerializer(read_only=True)
    class Meta:
        model=Userphone
        fields = '__all__'

class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields= '__all__'

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useraddress
        fields= '__all__'

class AddressSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Useraddress
        fields = '__all__'

class AddressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Addresstype
        depth=1
        fields = '__all__'

class AddressSerializerGet(serializers.ModelSerializer):
    address_type = AddressTypeSerializer(read_only=True)
    class Meta:
        model = Useraddress
        # depth = 1
        fields = '__all__'

class UserPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userphone
        fields= '__all__'

class PageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pagedata
        fields='__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self, clean_data):
        user_obj = User.objects.create(email=clean_data['email'],
                                       password=clean_data['password'])

