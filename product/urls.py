from django.urls import path
from . import views


urlpatterns = [
    path("category/<slug:slug_name>/",views.show_category,name="show_category"),
    path("cart/add/<int:product_id>/",views.add_item,name="add_item"),
    path("cart/delete/<int:product_id>/",views.delete_item,name="delete_item"),
    path("showcart/",views.show_cart,name="show_cart"),
]
