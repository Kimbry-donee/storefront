from django.contrib import admin
from .models import Product, Room, Topic, Message 


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(Product, ProductAdmin)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
