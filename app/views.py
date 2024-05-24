from django.shortcuts import render

from django.http import HttpResponse

from app.forms import *

''' in case of using model forms we don't need to import models again in our views as we are using model forms so it will take care of that'''

# Create your views here.


def insert_topic(request):
    ETFO=Topicform()            # TO CREATE INPUT FIELDS
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            TFDO.save()                # INSTEAD OF GETTING EACH TIME INPUT FIELD DATA WE USE TO DO IN DJNAGO,NORMAL HTML FORM  HERE WE DON'T NEED TO DO THAT MY MODELFORM IS FRESPONSIBLE FOR THAT SO HERE WE  CAN DIRECTLY SAVE IT
            return HttpResponse('DATA INSERTED SUCCESSFULLY')
        else:
            return HttpResponse('INVALID DATA INSERTION')

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO=Webpageform()                    # TO CREATE INPUT FIELDS
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=Webpageform(request.POST)
        if WFDO.is_valid():
            WFDO.save()                        # INSTEAD OF GETTING EACH TIME INPUT FIELD DATA WE USE TO DO IN DJNAGO,NORMAL HTML FORM  HERE WE DON'T NEED TO DO THAT MY MODELFORM IS FRESPONSIBLE FOR THAT SO HERE WE  CAN DIRECTLY SAVE IT
            return HttpResponse('DATA INSERTED SUCCESSFULLY')
        else:
            return HttpResponse('INVALID DATA INSERTION')
            
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    EAFO=Accessform()                    # TO CREATE INPUT FIELDS
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=Accessform(request.POST)
        if AFDO.is_valid():
            AFDO.save()                    # INSTEAD OF GETTING EACH TIME INPUT FIELD DATA WE USE TO DO IN DJNAGO,NORMAL HTML FORM  HERE WE DON'T NEED TO DO THAT MY MODELFORM IS FRESPONSIBLE FOR THAT SO HERE WE  CAN DIRECTLY SAVE IT
            return HttpResponse('DATA INSERTED SUCCESSFULLY')
        else:
            return HttpResponse('INVALID DATA INSERTION')
    return render(request,'insert_access.html',d)