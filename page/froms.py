from django.forms import ModelForm
from .models import Carousel




class CarouselForm(ModelForm):
    class Meta:
        model=Carousel
        fields='__all__'