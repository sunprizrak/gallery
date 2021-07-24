from django.views.generic import ListView, DetailView
from .models import Virtual


class VirtualView(ListView):
    model = Virtual
    template_name = 'virtual/virtual.html'
    context_object_name = 'virtual'
    extra_context = {
        'title': 'Виртуальная выставка',
    }


class VirtualDetailView(DetailView):
    model = Virtual
    template_name = 'virtual/virtual_detail.html'
    context_object_name = 'virtual_detail'
    extra_context = {
        'title': 'Виртуальная выставка',
    }
