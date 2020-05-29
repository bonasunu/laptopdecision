from django.shortcuts import render
from .models import Laptop
from .filters import LaptopFilter
from django.views.generic import ListView, DetailView

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

def help_me_choose(request):
    return render(request, 'app/help-me-choose.html')

def laptop(request, slug):
    try:
      laptop = Laptop.objects.get(slug=slug)
    except Laptop.DoesNotExist:
      raise Http404("Laptop does not exist")

    context = {
      "laptop": laptop,
    }
    
    return render(request, "app/laptop.html", context)