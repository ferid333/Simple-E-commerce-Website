from django.shortcuts import redirect, render
from .models import Carousel
from .froms import CarouselForm
from product.models import Category,Product,ShopingCart
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def index(request):
    carousels=Carousel.objects.filter(status="published")
    categories=Category.objects.filter(status="published").order_by("title")
    products=Product.objects.filter(is_home=True).order_by("title")
    try:
      showcart_items=ShopingCart.objects.get(user=request.user).items.all()
    except:
        showcart_items=None 
    context={
        "carousels":carousels,
        "categories":categories,
        "products":products,
        "showcart_items":showcart_items
    }
    return render(request,"index.html",context)


@staff_member_required
def carausel_list(request):
    carousels=Carousel.objects.all().order_by("-id")
    context={
        "carousels":carousels
    }
    return render(request,"manage/carousel_list.html",context)    

@staff_member_required
def carausel_create(request):
    form=CarouselForm()
    if request.method=="POST":
        form=CarouselForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("carousel_create")
    context={
        'form':form,
        "title":"Carousel Creating Form"
    }
    return render(request,"manage/form.html",context)

@staff_member_required
def carausel_update(request,id):
    carousel=Carousel.objects.get(id=id)
    form=CarouselForm(instance=carousel)
    if request.method=="POST":
        form =CarouselForm(request.POST, instance=carousel)
        if form.is_valid:
            form.save()
            return redirect("carousel_list")
    context={
        "form":form,
        "title":"Carousel Update Form"
    }
    return render(request,"manage/form.html",context)    