# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import json
from .models import Messages
from .forms import UserLoginForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (authenticate,
                                 get_user_model,
                                login, logout,
                                 )
# Create your views here.
def index(request):
    Message = Messages.objects.all().order_by('-id')
    user = request.user
    context = {
        "messages": Message,
        "user":user
    }
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

def login_view(request):
    title = 'login'
    print request.POST
    form = UserLoginForm(request.POST or None)
    print form
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)  # gets the user itseld
        login(request, user)
        print(request.user.is_authenticated())
        return redirect('index')
    return render(request, 'registration/login.html', {'form': form, 'title': 'BILLBOARD'})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print form
        print form.cleaned_data
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('index')
        else:
            print"not working"
            return redirect('index')

    else:
        form = UserCreationForm()
        return render(request, "registration/registration.html", {'form': form})

