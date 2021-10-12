from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'main'


urlpatterns = [
    path('', views.product_list, name='product_list'),
]

