from django.contrib import admin
from .models import Page,Carousel
# Register your models here.



class CarouselAdmin(admin.ModelAdmin):
    list_display=["title","status","cover_image",]

admin.site.register(Page)
admin.site.register(Carousel,CarouselAdmin)