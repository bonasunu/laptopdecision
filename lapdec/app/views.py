from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def laptops(request):
    return render(request, 'app/laptops.html')

def finder(request):
    return render(request, 'app/finder.html')

def comparison(request):
    return render(request, 'app/comparison.html')