from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Inspection


class InspectionListView(ListView):
    model = Inspection
    paginate_by = 100


class InspectionView(DetailView):
    model = Inspection


class InspectionCreate(CreateView):
    model = Inspection
    fields = ['title', 'frequency', 'status', 'date_next_due', 'procedure', 'estimated_cost', 'assigned_to']
    success_url = reverse_lazy('inspection_list')


class InspectionUpdate(UpdateView):
    model = Inspection
    fields = ['title', 'frequency', 'status', 'date_next_due', 'procedure', 'estimated_cost', 'assigned_to']
    success_url = reverse_lazy('inspection_list')

class InspectionDelete(DeleteView):
    model = Inspection
    success_url = reverse_lazy('inspection_list')