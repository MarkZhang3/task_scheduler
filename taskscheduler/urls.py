from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_date/<int:year>/<int:month>/<int:day>', views.get_date, name='get_date'),
    path('get_previous/<int:yy>/<int:mm>', views.get_previous, name='get_previous'),
    path('get_next/<int:yy>/<int:mm>', views.get_next, name='get_next'),
    path('add_event/', views.add_event, name="add_event"),
    path('event_details/<int:id>', views.event_details, name='event_details'),
    path('edit_event/<int:id>', views.edit_event, name='edit_event'),
    path('index_event_list/<int:year>/<int:month>/<int:day>', views.index_event_list, name='index_event_list'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]