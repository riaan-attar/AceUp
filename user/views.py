from django.shortcuts import render ,redirect, HttpResponse
from .models import*
from django.templatetags.static import static
import os
# Create your views here.
def landing(request):
    return render(request, 'index.html')


    

def displayNotes(request):
     note = notes.objects.all()
     return render(request , "notes.html",{"notes":note})
     
    #  print(notesa)
    

def reader(request,pk):

    file_link = notes.objects.get(id=pk)
    file_l = file_link.url.name
    filea= os.path.basename(file_l)
    filea = 'notes/'+filea
    file_l = static(filea)
    return render(request,'reader.html',{"file":file_l})


        



def displayTesti(request):
    testi = testimonial.objects.all()
    return render(request , "showTesti.html",{"testi":testi})

def contact(request):
    return render(request,'contact.html')



