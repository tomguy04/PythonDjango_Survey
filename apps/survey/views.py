# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    # response = "Hello, I am your first request!"
    return render(request,"survey/form.html")

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    if 'counter' in request.session.keys():
        request.session['counter']+=1
    else:
        request.session['counter']=0
    return redirect('/result')

def result(request):
    return render(request,"survey/data.html")
    
