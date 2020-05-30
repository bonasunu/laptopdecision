from django.shortcuts import render, redirect
from .models import Laptop
from .filters import LaptopFilter
from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):

    laptops = Laptop.objects.all()
    latest = Laptop.objects.all()[:3]

    context = {
        'laptops': laptops,
        'latest': latest
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

def result(request):

    if request.method == 'POST':

        mobility = request.POST.get('mobility_answer')
        location = request.POST.getlist('location_answer')
        activity = request.POST.getlist('activity_answer')
        result = ''

        if mobility == 'everyday':
            results = Laptop.objects.all().filter(category='Ultrabook')
        elif mobility == 'few':
            result = Laptop.objects.all().filter(category='Home/Business')
        else:
            results = Laptop.objects.all().filter(category='Gaming')

        context = {
            'mobility': mobility,
            'location': location,
            'activity': activity,
            'result': result
        }

        print(result)
    
        return render(request, 'app/result.html', context)

    return render(request, 'app/result.html')

def laptop(request, slug):
    try:
      laptop = Laptop.objects.get(slug=slug)
    except Laptop.DoesNotExist:
      raise Http404("Laptop does not exist")

    context = {
      "laptop": laptop,
    }
    
    return render(request, "app/laptop.html", context)