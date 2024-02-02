from django.db import models

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    order_date = models.DateTimeField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Order'
    
    def __str__(self) -> str:
        return f'{self.order_id} {self.order_date} {self.total_amount} {self.status}'

class Orderservices(models.Model):
    order_service_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, models.DO_NOTHING)
    service = models.ForeignKey('Services', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'OrderServices'
    
    def __str__(self) -> str:
        return f'{self.order_id} {self.order} {self.service}'

class Phonetype(models.Model):
    phone_type_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'PhoneType'

    def __str__(self) -> str:
        return f'{self.phone_type_id}'

class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_description = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Services'

    def __str__(self) -> str:
        return f'{self.service_id} {self.service_description} {self.price}'

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    pass_word = models.CharField(max_length=40, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    user_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'
    
    def __str__(self) -> str:
        return f'{self.user_id} {self.first_name} {self.last_name} {self.user_name}'


class Useraddress(models.Model):
    user_address_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    address_1 = models.CharField(max_length=30, blank=True, null=True)
    address_2 = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    st = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserAddress'
    
    def __str__(self) -> str:
        return f'{self.user} {self.user_address_id} {self.address_1} {self.address_2} {self.city} {self.st} {self.zip} {self.country}'

class Userphone(models.Model):
    user_phone_id = models.IntegerField(primary_key=True)
    phone_type = models.ForeignKey(Phonetype, models.DO_NOTHING)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserPhone'
    
    def __str__(self) -> str:
        return f'{self.user} {self.user_phone_id} {self.phone_type} {self.phone_number} {self.created_date}'