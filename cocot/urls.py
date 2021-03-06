"""cocot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from monyong.views import task, check, check_progress
from monyong.views import check_log

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', task, name='home'),
    url(r'^check/(?P<task_id>\d+)$', check, name='check'),
    url(r'^check-progress/(?P<task_id>\d+)$', check_progress, name='check_progress'),
    url(r'^check-log/(?P<task_id>\d+)/(?P<pos>\d+)$', check_log, name='check_log')
]
