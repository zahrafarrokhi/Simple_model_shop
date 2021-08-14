from django.contrib import admin
from .models import Product,Cart,CartItem
# Register your models here.
admin.site.register(Product)
# admin.site.register(Cart)
# admin.site.register(CartItem)

class CartItemInline(admin.TabularInline):
	model = CartItem
	raw_id_fields = ('product',)


class CartAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'payment_date ', 'is_paid ')
	list_filter = ('is_paid',)
	inlines = (CartItemInline,)

admin.site.register(Cart,CartAdmin)

