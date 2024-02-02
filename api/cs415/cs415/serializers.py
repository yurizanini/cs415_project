from rest_framework import serializers
from cs415.models import User, Order, Orderservices, Phonetype, Services, Useraddress, Userphone

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

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields= '__all__'

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useraddress
        fields= '__all__'

class UserPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userphone
        fields= '__all__'