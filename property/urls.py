from django.urls import path, include

from properties.views import *

urlpatterns = [
    path('property/', PropertyListView.as_view(), name='property-list'),
    path('property/<int:pk>', PropertyDetailView.as_view(), name='property-detail'),
    path('property/create', PropertyCreateView.as_view(), name='property-create'),
    path('property/<int:pk>/edit', PropertyUpdateView.as_view(), name='property-update'),
    path('property/<int:pk>/delete', PropertyDeleteView.as_view(), name='property-delete'),
]