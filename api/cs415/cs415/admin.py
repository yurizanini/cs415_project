from django.contrib import admin

from .models import Order, Orderservices, Phonetype, Services, User, Useraddress, Userphone, Pagedata

admin.site.register(Order)
admin.site.register(Orderservices)
admin.site.register(Phonetype)
admin.site.register(Services)
admin.site.register(User)
admin.site.register(Useraddress)
admin.site.register(Userphone)
admin.site.register(Pagedata)