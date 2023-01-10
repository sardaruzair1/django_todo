from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'Tasks'
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'Task'  

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('index')      

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('index')
class DeleteView(DeleteView):
    model = Task
    context_object_name = 'Task'      
    success_url = reverse_lazy('index')      