from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.

from django.views.generic.list import ListView

class TodolistListView(ListView):
    model = Todolist
    paginate_by = 3


from django.views.generic.detail import DetailView

class TodolistDetailView(DetailView):
    model = Todolist



from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
class TodolistCreateView(CreateView):
    model = Todolist
    fields = ['todo_title','todo_url','todo_priority','todo_completion']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'



from django.views.generic.edit import UpdateView
class TodolistUpdateView(UpdateView):
    model = Todolist
    fields = ['todo_title','todo_url','todo_priority','todo_completion']
    success_url = reverse_lazy('list')
    template_name_suffix = '_update'

from django.views.generic.edit import DeleteView


class TodolistDeleteView(DeleteView):
    model = Todolist
    success_url= reverse_lazy('list')