from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse

from .models import TODOList


class TODOListCreateView(CreateView):
    model = TODOList
    fields = ['name']

    def get_success_url(self, *args, **kwargs):
        return reverse('lists:home')


class TODOListView(ListView):
    model = TODOList
