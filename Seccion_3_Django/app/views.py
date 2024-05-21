from django.shortcuts import render
from .models import Producto
from django.views.generic import ListView


class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/producto_list.html'
    context_object_name = 'productos'
    paginate_by = 10
