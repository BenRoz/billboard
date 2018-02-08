# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import json
from .models import Messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    Message = Messages.objects.all().order_by('-id')
    context = {"messages": Message}
    return render(request, 'billboard_app/index.html', context)

def newform(request):
    Message = Messages.objects.all().order_by('-id')[:1]
    context = {"messages": Message,"current_date": datetime.datetime.now()}
    return render(request, 'billboard_app/newpost.html', context)

@csrf_exempt
def sent_msg(request):
    print "here"
    title = request.POST.get("title")
    msg = request.POST.get("msg")
    author = request.POST.get("author")
    message = Messages.objects.create(title=title, msg=msg, author=author, date=datetime.datetime.now())
    message.save()
    context = {"messages": message}
    return render(request, 'billboard_app/newpost.html', context)


@csrf_exempt
def delete_msg(request, id):
    print "inside delete msg"
    # id = request.POST.get("id_to_delete")
    msg = Messages.objects.get(id=id)
    msg.delete()
    context = {"messages": ""}
    return render(request, 'billboard_app/index.html', context)
