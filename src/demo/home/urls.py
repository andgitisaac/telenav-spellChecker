from django.urls import path

from . import views

urlpatterns = [
    path('history/', views.get_history, name='get_history'),
    path('add_query/', views.add_query, name='add_query'),
    path('search/', views.search, name='search'),
]