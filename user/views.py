from django.shortcuts import render ,redirect, HttpResponse
from .models import*
from django.templatetags.static import static
import os
# Create your views here.
def landing(request):
    return render(request, 'index.html')

def roadmapsview(request):
    roadmaplist = roadmaps.objects.all()
    return render(request, "roadmaps.html",{"roadmaps":roadmaplist})

def displayNotes(request):
     note = notes.objects.all()
     return render(request , "notes.html",{"notes":note})
     
    #  print(notesa)

def eventsview(request):
    return render(request,'events.html')

def communities(request):
    return render(request,'communities.html')

def reader(request,pk):

    file_link = notes.objects.get(id=pk)
    file_l = file_link.url.name
    filea= os.path.basename(file_l)
    filea = 'notes/'+filea
    file_l = static(filea)
    return render(request,'reader.html',{"file":file_l})

def displayTesti(request):
    testi = testimonial.objects.all()
    return render(request , "testimonials.html",{"testi":testi})

def contact(request):
    return render(request,'contact.html')


