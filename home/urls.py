from django.urls import path
from . import views
urlpatterns= [
    path('',views.Home_notlog,name='home')
]