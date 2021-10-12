from django.shortcuts import render
from .models import Product


def base(request):
    return render(
        request=request,
        template_name='main/base.html',
    )


def product_list(request):
    product = Product.objects.all()
    return render (request,'main/base.html', {'products': product})

