from products.models import Product
from courses.models import Courses
from users.models import User
from django.db import models





class Cart(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر ')
    payment_date = models.DateTimeField(auto_now_add=False,blank=True,null=True,verbose_name='تاریخ پرداخت ')
    total_price = models.IntegerField(default=0,blank=True,null=True,verbose_name='جمع کل ')
    discountCode = models.IntegerField(default=0,blank=True,null=True,verbose_name='تخفیف اعمال ')
    tracking_code = models.TextField(blank=True,null=True,verbose_name='کد پیگیری ')
    is_paid = models.BooleanField(default=False,blank=True,null=True,verbose_name='وضعیت پرداخت ')
    
    

    class Meta:
        verbose_name = 'سبد'
        verbose_name_plural = 'سبد خرید'

    def __str__(self):
        return f'{self.owner.get_full_name()}'


class Digital(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,verbose_name='خریدار ',related_name='digital_set')
    price = models.CharField(max_length=900,blank=True,null=True,verbose_name='قیمت ')
    payment_date = models.DateTimeField(auto_now_add=False, blank=True, null=True, verbose_name='تاریخ پرداخت ')
    is_paid = models.BooleanField(default=False,blank=True,null=True,verbose_name='وضعیت پرداخت ')
    slug = models.SlugField(max_length=900,blank=True,null=True,verbose_name='آدرس url ')
    product = models.ForeignKey(Product,blank=True,null=True,on_delete=models.CASCADE,verbose_name='محصول ')

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات دیجیتالی'

    def __str__(self):
        return f'{self.product.title} - Owner {self.cart.owner.get_full_name()}'




class Physical(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,verbose_name='خریدار ',related_name='physical_set')
    price = models.CharField(max_length=900,blank=True,null=True,verbose_name='قیمت ')
    reciver = models.CharField(max_length=900,blank=True,null=True,verbose_name='گیرنده ')
    PostalCode = models.CharField(max_length=900,blank=True,null=True,verbose_name='کد پستی ')
    payment_date = models.DateTimeField(auto_now_add=False, blank=True, null=True, verbose_name='تاریخ پرداخت ')
    is_paid = models.BooleanField(default=False,blank=True,null=True,verbose_name='وضعیت پرداخت ')
    address = models.TextField(blank=True,null=True,verbose_name='آدرس ')
    slug = models.SlugField(max_length=900,blank=True,null=True,verbose_name='آدرس url ')
    post_status = models.BooleanField(default=False,blank=True,null=True,verbose_name='وضعیت ارسال ')
    product = models.ForeignKey(Product,blank=True,null=True,on_delete=models.CASCADE,verbose_name='محصول ')

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات فیزیکی'

    def __str__(self):
        return f'{self.product.title} - Owner {self.cart.owner.get_full_name()}'



class Course(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,verbose_name='خریدار ',related_name='courses_set')
    price = models.CharField(max_length=900,blank=True,null=True,verbose_name='قیمت ')
    payment_date = models.DateTimeField(auto_now_add=False, blank=True, null=True, verbose_name='تاریخ پرداخت ')
    is_paid = models.BooleanField(default=False,blank=True,null=True,verbose_name='وضعیت پرداخت ')
    slug = models.SlugField(max_length=900,blank=True,null=True,verbose_name='آدرس url ')
    course = models.ForeignKey(Courses,blank=True,null=True,on_delete=models.CASCADE,verbose_name='دوره ')

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'

    def __str__(self):
        return f'{self.course.CourseName} - Owner {self.cart.owner.get_full_name()}'

