from django.contrib import admin
from django.urls import include, path

from maindata.views import carfollowingcard, invoice

# from .views import createvisitforreserve
app_name = 'maindata'

urlpatterns = [
    path('invoice/<int:pk>/', invoice, name="invoice"),
    path('carfollowingcard/<int:pk>/', carfollowingcard, name="carfollowingcard"),
    # path('createvisitforreserve/<int:pk>/', createvisitforreserve, name='createvisitforreserve'),
]



