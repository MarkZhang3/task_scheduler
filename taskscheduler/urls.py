from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_date/<int:year>/<int:month>/<int:day>', views.get_date, name='get_date'),
    path('get_previous/<int:year>/<int:month>/<int:day>', views.get_previous, name='get_previous'),
    path('get_next/<int:year>/<int:month>/<int:day>', views.get_next, name='get_next'),
    
]