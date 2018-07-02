# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import threading
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Value
from django.db.models.functions import Concat
from django.db.models import F

from multiprocessing import Process
from multiprocessing import active_children
from time import sleep
from uuid import uuid4
from .models import Task

def process(task):
    for a in range(20):    
        sleep(1)
        Task.objects.filter(id=task).update(
            last_line_log = F('last_line_log')+1,
            progress=a * 4,
            log=Concat('log', Value(str(a * 4) + "<br/>")))
    Task.objects.filter(id=task).update(state="D", progress=100)
    print task
    
def task(request):
    task = Task.objects.create(name=uuid4().hex, state="S")
    proc = Process(target=process, args=(task.id,), name=task.name)
    proc.daemon = True
    proc.start() 
    return render(request,"index.html", {"task": task})

def check(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, "check.html", {"task": task})

def check_progress(request, task_id):
    ps_list = [p.name for p in active_children()]
    task = Task.objects.get(id=task_id)
    if task.name in ps_list:
        return HttpResponse(task.progress)
    else:
        if task.state != "D":
            Task.objects.filter(id=task_id).update(state="X",progress=100)
            return HttpResponse(100)
        else:
            return HttpResponse(100)
        
def check_log(request, task_id, pos):
    task = Task.objects.get(id=task_id)
    data = task.log.split("<br/>")
    del data[-1]
    resp = {
        "line": task.last_line_log,
        "result": "<br/>".join(data[int(pos):int(task.last_line_log)]) + "<br/>"
    }
    return JsonResponse(resp)