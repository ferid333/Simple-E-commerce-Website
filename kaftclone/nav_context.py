from multiprocessing import context
from product.models import Category
from page.models import Page


def datas(request):
    categories=Category.objects.filter(status="published").order_by('title')
    pages=Page.objects.filter(status="published").order_by('title')
    context={
        "categories":categories,
        "pages":pages
    }
    return context
