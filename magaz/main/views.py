from .models import Product
from django.views.generic.list import ListView
from . import views


class ProductListView(ListView):
    template_name = 'main/product_list.html'
    context_object_name = 'products'
    model = Product

