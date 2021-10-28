from . import views
from django.urls import path


app_name = 'main'


urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('login/', views.LoginView.as_view(), name='Login'),
    path('signup/', views.Register.as_view(), name='signup'),
]

