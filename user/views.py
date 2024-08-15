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
    return render(request , "testimonials.html",{"testi":testi})


def testEntry(request):   
    if request.method == "POST" :
        name = request.POST.get("title")
        testi = request.POST.get("description")
        git = request.POST.get("github")
        linkedin = request.POST.get("linkedin")
        image = request.FILES.get("photo")
        
        if name and testi and git and linkedin and image:
            a = testimonial.objects.create (
            name = name,
            testi = testi,
            git =git,
            linkdin =linkedin,
            image = image )
            a.save()
        else:
            return HttpResponse("Please fill all fields")
    return render(request, 'testEntry.html')



def contact(request):
    return render(request,'contact.html')


