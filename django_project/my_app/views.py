from django.shortcuts import render
from django.http import HttpResponse
from my_first_app.models import *
# Create your views here.
def index(request):
    webpages_list = AcessRecord.objects.order_by('date')
    date_dict = {'acess_records': webpages_list}
    return render(request, 'my_first_app/index.html', context=date_dict)
