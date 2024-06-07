from .models import *
from django.forms import ModelForm


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'