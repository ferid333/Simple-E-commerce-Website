from django.shortcuts import render,redirect
from .models import Category,Product,ShopingCart
from django.http import JsonResponse
# Create your views here.


def show_category(request,slug_name):
    category=Category.objects.get(slug=slug_name)
    try:
      showcart_items=ShopingCart.objects.get(user=request.user).items.all()
    except:
      showcart_items=None 
    items=Product.objects.filter(
        category=category,
        stock__gte=1
    )
    context={
        "category":category,
        "items":items,
        "showcart_items":showcart_items
    }
    return render(request,"product/show_category.html",context)

def add_item(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
      shopcart=ShopingCart.objects.get(user=request.user)
      shopcart.items.add(product) 
    except:
     shopcart=ShopingCart.objects.create(user=request.user)
     shopcart.items.add(product) 
    return JsonResponse({
        "message":"Go Cart"
    })
def show_cart(request):
    try:
        shopcart=ShopingCart.objects.get(user=request.user)
    except:
        shopcart=ShopingCart.objects.create(user=request.user)
    
    items=shopcart.items.all()
    context={
        "shopcart":shopcart,
        "items":items
    }
    return render(request,"product/cart.html",context)
def delete_item(request,product_id):
    product=Product.objects.get(id=product_id)
    shopcart=ShopingCart.objects.get(user=request.user)
    shopcart.items.remove(product) 
    return redirect("show_cart")  