from django.contrib import admin
from .models import Room,Dish,Offer,Reservation
# Register your models here.

admin.site.register(Room)
admin.site.register(Dish)
admin.site.register(Offer)
admin.site.register(Reservation)