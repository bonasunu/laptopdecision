from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('laptops', views.laptops, name='laptops'),
    path('finder', views.finder, name='finder'),
    path('comparison', views.comparison, name='comparison'),
]