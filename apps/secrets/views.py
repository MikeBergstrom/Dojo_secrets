# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import datetime
from .models import Secret
from ..login.models import User
from django.db.models import Count


def secrets(request):
    try:
    # secrets = Secret.objects.annotate(timediff=Secret.objects.timediff())
        secrets = Secret.objects.annotate(likecount=Count('like')).order_by('-created_at')[:5]
        context = {
            'secrets':secrets,
            'current_user': User.objects.get(id=request.session['id'])
            }
        return render(request, 'secrets/secrets.html', context)
    except:
        return redirect('/')
    # print users, secrets
    

def process(request):
    Secret.objects.create(secret=request.POST['secret'], user=User.objects.get(id=request.session['id']))
    return redirect('/secrets')

def like(request, source, id):
    secret = Secret.objects.get(id=id)
    user = (User.objects.get(id=request.session['id']))
    secret.like.add(user)
    print user.likes
    print user.first_name
    print secret.secret
    print secret.like.all()
    if source == "home":
        return redirect ('/secrets')
    else:
        return redirect ('/popular')

def delete(request, source, id):
    Secret.objects.get(id=id).delete()
    if source == "home":
        return redirect ('/secrets')
    else:
        return redirect ('/popular')
def popular(request):
    try:
        popsecrets = Secret.objects.annotate(likecount=Count('like')).order_by('-likecount')[:5]
        context = {
            'secrets':popsecrets,
            'current_user': User.objects.get(id=request.session['id'])
        }
        return render(request, 'secrets/popular.html', context)
    except:
        return redirect('/')

def logout(request):
    request.session['id'] = None
    request.session['first'] = None
    return redirect ('/')