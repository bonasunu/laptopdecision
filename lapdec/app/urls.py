from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('finder', views.finder, name='finder'),
    path('help-me-choose', views.help_me_choose, name='help'),
    path('<slug:slug>', views.laptop),
    path('help-me-choose/result', views.result, name='result'),
]