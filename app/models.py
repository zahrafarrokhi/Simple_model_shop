from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='عنوان')
    price = models.IntegerField(verbose_name='قیمت')
    active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    quantity = models.IntegerField(verbose_name='تعداد')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name


class Cart(models.Model):
    # shift+alt,inter (import User) or (alt+inter)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts', related_query_name='cart')
    is_paid = models.BooleanField(verbose_name='پرداخت شده / نشده')
    # STATUS_CHOICES = [
    #     ('OPEN', 'open'),
    #     ('CLOSED', 'closed')
    # ]
    # status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='open')
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'

    def __str__(self):
        return self.user.username

    @property
    def total_price(self):
        total = 0
        for item in self.items.all():
             total += (item.price * item.quantity)
        return int(total)

    # if cart has discount field
    # @property
    # def get_total_price(self):
    #     total = sum(item.total_price() for item in self.items.all())
    #     if self.discount:
    #         discount_price = (self.discount / 100) * total
    #         return int(total - discount_price)
    #     return total

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', related_query_name='item', verbose_name='سبد خرید')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='carts',related_query_name='cart',verbose_name='محصول')
    quantity = models.IntegerField(verbose_name='تعداد')
    price = models.IntegerField(verbose_name='قیمت محصول')

    class Meta:
        verbose_name = 'جزییات محصول'
        verbose_name_plural = 'اطلاعات جزییات محصولات'

    def __str__(self):
        return self.product.name

    @property
    def total_price(self):
        return int(self.price * self.quantity)





