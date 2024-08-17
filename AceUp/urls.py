"""AceUp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views
from admin.views import *
from learnGpt.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing,name ="landing"),
    path('displayNotes/',views.displayNotes,name ="display"),
    path('displayDocs/',views.displayDocs,name ="displayDocs"),
    path('roadmapsview/', views.roadmapsview, name='roadmapsview'),
    path('addnotes/',noteEntry,name ="upload"),
    path("displayTesti/", views.displayTesti, name = "displayTesti"),
    path("testEntry/", testEntry, name = "testEntry"),
    path("contactus/",views.contact,name = "contact"),
    path('reader/<int:pk>/',views.reader,name='reader'),
    path('pdfreader/<int:pk>/',views.pdfreader,name='pdfreader'),
    path('docreader/<int:pk>/',views.docreader,name='docreader'),
    path('adddocs/',views.adddocs,name='adddocs'),
    path('gen/', gen , name = 'gen'),
    path('communities/',views.communities,name = 'communities'),
    path('events/',views.eventsview,name = 'events'),
    path('upload_pdfs/', upload_pdfs, name='upload_pdfs'),
    path('know_more/',views.eventsinfo, name = 'eventinfo'),
    path('event_upload/', event_upload, name = 'event_upload'),
]
