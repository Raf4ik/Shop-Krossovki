from . import views
from django.urls import path


app_name = 'main'


urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
]
