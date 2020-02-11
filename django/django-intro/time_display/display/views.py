from django.shortcuts import render, HttpResponse
import datetime
from time import gmtime, strftime

def index(request):
    return render(request, 'index.html')

def time(request):
    # current = datetime.datetime.now()
    # context = {
    #     'time': current
    # }
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }

    return render(request,'index.html', context)