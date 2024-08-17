from django.contrib import admin
from .models import Category,Product,ShopingCart
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'gender',
        'status', 
        'updated_at',
    )
    list_filter = ('status', 'gender', )
    list_editable = (
        'title',
        'status', 
    )



admin.site.register(Category,CategoryAdmin)
admin.site.register(Product)
admin.site.register(ShopingCart)