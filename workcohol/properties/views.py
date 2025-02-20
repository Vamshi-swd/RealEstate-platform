# properties/views.py
from django.shortcuts import render
from .models import Property

def properties_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/properties_list.html', {'properties': properties})