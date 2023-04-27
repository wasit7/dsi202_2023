from django.contrib import admin
from .models import Product, Profile, Order, Item

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'unit_price', 'weight','image')
    list_filter = ('weight',)
    search_fields = ('name',)
admin.site.register(Product, ProductAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'name', 'postcode')
    list_filter = ('postcode',)
    search_fields = ('user', 'name',)
admin.site.register(Profile, ProfileAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','profile', 'reciept')
    list_filter = ('profile',)
    search_fields = ('profile',)
admin.site.register(Order, OrderAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','order', 'product', 'quantity')
    list_filter = ('order',)
    search_fields = ('order',)
admin.site.register(Item, ItemAdmin)
