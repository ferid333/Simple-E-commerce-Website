from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="home"),
    path("manage/carousel/list",views.carausel_list,name="carousel_list"),
    path("manage/carousel/create",views.carausel_create,name="carousel_create"),
    path("manage/carousel/<int:id>",views.carausel_update,name="carousel_update"),
]
