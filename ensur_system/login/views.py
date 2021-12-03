from django.shortcuts import render
from django.http import HttpResponse
from login.models import YwryCustomer
# Create your views here.

def index(request):
    ywrycustomer =YwryCustomer.objects.all()
    return HttpResponse(ywrycustomer)