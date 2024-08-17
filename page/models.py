from django.db import models
from django.utils.text import slugify
# Create your models here.


STATUS=[
    ("draft","draft"),
    ("published","published"),
    ("deleted","deleted")
]
class Page(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(null=True,blank=True)
    cover_image=models.ImageField(
        null=True,
        upload_to="page",
        blank=True
    )
    status=models.CharField(max_length=10,choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(args,kwargs)

class Carousel(models.Model):
    title=models.CharField(max_length=200)
    cover_image=models.ImageField(
        null=True,
        upload_to="carousel",
        blank=True
    )
    status=models.CharField(max_length=10,choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)        