from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse

from .models import TODOList


class TODOListCreateView(CreateView):
    model = TODOList
    fields = ['name']

    def get_success_url(self, *args, **kwargs):
        return reverse('lists:home')


class TODOListView(ListView):
    model = TODOList


class TODOListDetailView(DetailView):
    model = TODOList