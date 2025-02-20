# properties/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Property
from .forms import PropertyForm
from django.core.paginator import Paginator

def property_list(request):
    properties = Property.objects.all()
    paginator = Paginator(properties, 10)  # Show 10 properties per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'properties/property_list.html', {'page_obj': page_obj})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'properties/property_detail.html', {'property': property})

def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user
            property.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/property_form.html', {'form': form})

def property_edit(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm(instance=property)
    return render(request, 'properties/property_form.html', {'form': form})

# properties/views.py
def personalized_recommendations(request):
    if request.user.is_authenticated:
        preferences = request.session.get('preferences', {})
        property_type = preferences.get('property_type', '')
        price_min = preferences.get('price_min', '')
        price_max = preferences.get('price_max', '')

        properties = Property.objects.all()
        if property_type:
            properties = properties.filter(property_type__icontains=property_type)
        if price_min:
            properties = properties.filter(price__gte=price_min)
        if price_max:
            properties = properties.filter(price__lte=price_max)
    else:
        properties = Property.objects.all()[:10]  # Default recommendations

    return render(request, 'properties/recommendations.html', {'properties': properties})

def chat_room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})