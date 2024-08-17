from django.shortcuts import render ,redirect, HttpResponse,get_object_or_404
from .models import*
from django.templatetags.static import static
import os
import markdown2 
# Create your views here.
def landing(request):
    return render(request, 'index.html')

def roadmapsview(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        if query:
            roadmaplist = roadmaps.objects.filter(title__icontains=query)
        else:
            roadmaplist = roadmaps.objects.all()
    else:
        roadmaplist = roadmaps.objects.all()

    return render(request, 'roadmaps.html', {'roadmaps': roadmaplist})

def displayNotes(request ):
     note = notes.objects.all()
     return render(request , "notes.html",{"notes":note})
     
    #  print(notesa)

def eventsview(request):
    event_list = events.objects.all()
    return render(request,'events.html',{'event_list': event_list})

def eventsinfo(request, event_id):
    event_main = get_object_or_404(events, pk=event_id)
    event_details = event.objects.filter(event=event_main)
    event_main.description = markdown2.markdown(event_main.description)
    return render(request, 'event_detail.html', {'event_main': event_main,'event_details': event_details})

    




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

def pdfreader(request,pk):
    file_link = roadmaps.objects.get(id=pk)
    file_l = file_link.url.name
    filea= os.path.basename(file_l)
    filea = 'roadmaps/'+filea
    file_l = static(filea)
    return render(request,'reader.html',{"file":file_l})


