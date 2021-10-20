from .models import Product
from django.views.generic.list import ListView
from . import views


class ProductListView(ListView):
    template_name = 'main/product_list.html'
    context_object_name = 'products'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()
        return context
