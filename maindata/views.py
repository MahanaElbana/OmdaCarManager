from companyinfo.models import CompanyInfo
from .models import Category, Car, Client, SellOperation
from django.shortcuts import render,redirect
from django.urls import reverse
from admin_interface.models import Theme

def invoice(request, pk):
    obj = SellOperation.objects.get(id = pk)
    client = Client.objects.filter(selloperation = obj)[0]
    car = obj.car
    #------------------------------------
    companyinfo = CompanyInfo.objects.last()
    #------------------------------------
    theme = Theme.objects.get(active = 1)
    logo_url = None
    if theme.logo:
        logo = theme.logo
        logo_url = logo.url
    #-----------------------------------
    context = {
            'sellprocess_id' : pk,
            'sellprocess' : obj,
            'client' : client,
            'car' : car,
            'logo_url' : logo_url,
            'companyinfo' : companyinfo,
        }
    return render(request,'maindata/invoice.html' ,context)

def carfollowingcard(request, pk):
    car = Car.objects.get(id = pk)
    #------------------------------------
    companyinfo = CompanyInfo.objects.last()
    #------------------------------------
    theme = Theme.objects.get(active = 1)
    logo_url = None
    if theme.logo:
        logo = theme.logo
        logo_url = logo.url
    #-----------------------------------
    context = {
            'car' : car,
            'logo_url' : logo_url,
            'companyinfo' : companyinfo,
        }
    return render(request,'maindata/followingcard.html' ,context)
