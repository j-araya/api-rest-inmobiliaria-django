from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from properties.models import Property
from properties.forms import PropertyForm

# Create your views here.

# Booking views
class PropertyListView(ListView):
    model = Property
    template_name = 'properties/list.html'
    context_object_name = 'properties'
    queryset = Property.objects.all()

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'properties/detail.html'

class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'properties/form.html'
    success_url = reverse_lazy('property-list')

class PropertyUpdateView(UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = 'properties/form.html'
    success_url = reverse_lazy('property-list')

class PropertyDeleteView(DeleteView):
    model = Property
    template_name = 'properties/confirm-delete.html'
    success_url = reverse_lazy('property-list')