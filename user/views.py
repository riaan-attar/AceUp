from django.shortcuts import render ,redirect, HttpResponse
from .models import*

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

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
     notes = notes.objects.all()
     return render(request , "show.html",{"notes":notes})

        

