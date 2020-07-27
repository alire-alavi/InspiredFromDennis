from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICE = (
    ('آقای','آقای'),
    ('خانم', 'خانم')
)

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    province = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    GmBH = models.CharField(max_length=64, blank=True, null=True)
    forname = models.CharField(max_length=64, blank=True, null=True)
    nachname = models.CharField(max_length=64, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True , null=True, choices=GENDER_CHOICE)


    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('جت پرینتر','جت پرینتر'),
        ('کیسه پر کن','کیسه پر کن'),
        ('خط تولید','خط تولید'),
    )
    name = models.CharField(max_length=64, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=64, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
			('تایید شده', 'تایید شده'),
			('در انتظار تایید', 'در انتظار تایید'),
			('رد شده', 'رد شده'),
			)
    confirmed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
	    return f"order of {self.product.name}"