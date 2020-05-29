from django.shortcuts import render
from .models import Laptop
from .filters import LaptopFilter

# Create your views here.
def index(request):

    laptops = Laptop.objects.all()

    context = {
        'laptops': laptops
    }

    return render(request, 'app/index.html', context)

def finder(request):

    laptops = Laptop.objects.all()
    laptops_filter = LaptopFilter(request.GET, queryset = laptops)

    context = {
        'laptops': laptops,
        'filter': laptops_filter
    }

    return render(request, 'app/finder.html', context)

def comparison(request):

    laptops = Laptop.objects.all()

    context = {
        'laptops': laptops
    }

    return render(request, 'app/comparison.html', context)