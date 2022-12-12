from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_date/<int:year>/<int:month>/<int:day>', views.get_date, name='get_date'),
]