from django.db import models
from django.utils.text import slugify
from page.models import STATUS
from django.contrib.auth.models import User
from django.db.models.signals import  m2m_changed
from django.dispatch import receiver
# Create your models here.

GENDERS=[
    ("man","man"),
    ("woman","woman"),
    ("unisex","unisex"),
]

class Category(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(null=True,blank=True)
    gender=models.CharField(default="unisex",choices=GENDERS,max_length=8)
    status=models.CharField(max_length=10,choices=STATUS,default="draft")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(args,kwargs)


class Product(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    stock=models.PositiveSmallIntegerField(default=0)
    price=models.FloatField()
    cover_image = models.ImageField(
        upload_to='product',
        null=True,
        blank=True,
    )
    is_home = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(args,kwargs)  

class ShopingCart(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE
    )
    items = models.ManyToManyField(Product,null=True)
    total_price = models.FloatField(default=0)
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.pk}"


    def total_price_update(self):
        total_price=0
        for x in list(self.items.values()):
            total_price+=x["price"]
        self.total_price=total_price    
        self.save()

@receiver(m2m_changed, sender=ShopingCart.items.through)
def shopping_card_receiver(sender, instance, *args, **kwargs):
    instance.total_price_update()