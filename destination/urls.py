from django.urls import path
from . import views
urlpatterns= [
    path('destinationpID/',views.destination_view,name='page')
]