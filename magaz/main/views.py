from .models import Product
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy



class ProductListView(ListView):
    template_name = 'main/product_list.html'
    context_object_name = 'products'
    model = Product


class Login(LoginView):
    template_name = 'registration/login.html'
    contex_object_name = 'login'
    success_url = reverse_lazy('login')


class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

    def form_valid(self, form):
        form.save()
        return super(Register, self).form_valid(form)






