from django.urls import path
from .views import Usermain
urlpatterns = [
    path('mainuser/',Usermain,name='userhome')
]