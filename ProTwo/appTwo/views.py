from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import *

# Create your views here.
def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'appTwo/help.html',context=helpdict)

def index(request):
    return render(request,'appTwo/index.html')

def user(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'appTwo/users.html',context=user_dict)
