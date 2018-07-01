# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import threading
from django.shortcuts import render
from django.http import HttpResponse
from multiprocessing import Process
from time import sleep
from uuid import uuid4
from .models import Task

def process(task):
    for a in range(20):    
        sleep(2)
        Task.objects.filter(id=task).update(progress=a * 4)
    Task.objects.filter(id=task).update(state="D", progress=100)
    print task
    

def task(request):
    task = Task.objects.create(name=uuid4().hex, state="S")
    thread = threading.Thread(target=process, args=(task.id,))
    thread.daemon = True
    thread.start() 
    return render(request,"index.html", {"task": task})

def check(request, task_id):
    return render(request, "check.html", {"id": task_id})

def check_progress(request, task_id):
    task = Task.objects.get(id=task_id)
    return HttpResponse(task.progress)