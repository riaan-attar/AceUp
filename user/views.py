from django.shortcuts import render ,redirect, HttpResponse
from .models import*
from django.templatetags.static import static
import os
# Create your views here.
def landing(request):
    return render(request, 'index.html')

def noteEntry(request):
    if request.method == "POST" :
        title = request.POST.get("title")
        year = request.POST.get("year")
        subject = request.POST.get("subject")
        url = request.FILES.get("url")
        if title and subject and year and url :
            n = notes.objects.create (
            title = title,
            year = year,
            subject = subject,
            url = url )
            n.save()
        else:
            return HttpResponse("Please fill all fields")
    return render(request, 'noteEntry.html')
    

def displayNotes(request):
     note = notes.objects.all()
    #  print(notesa)
     return render(request , "notes.html",{"notes":note})

def reader(request,pk):

    file_link = notes.objects.get(id=pk)
    file_l = file_link.url.name
    filea= os.path.basename(file_l)
    filea = 'notes/'+filea
    file_l = static(filea)
    return render(request,'reader.html',{"file":file_l})


        

