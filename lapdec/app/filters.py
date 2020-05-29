from .models import Laptop
import django_filters

class LaptopFilter(django_filters.FilterSet):
    
    brand = django_filters.CharFilter(lookup_expr='icontains')
    item_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:

        model = Laptop
        
        fields = ['brand', 'category', 'item_name', ]