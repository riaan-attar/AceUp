from django.shortcuts import render ,redirect,HttpResponse
from user.models import * 
# Create your views here.
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

def testEntry(request):   
    if request.method == "POST" :
        title = request.POST.get("title")
        testi = request.POST.get("description")
        git = request.POST.get("github")
        linkedin = request.POST.get("linkedin")
        image = request.FILES.get("photo")

        if title and testi and git and linkedin and image:
            a = testimonial.objects.create (
            title = title,
            testi = testi,
            git =git,
            linkdin =linkedin,
             image = image )
            a.save()
        else:
            return HttpResponse("Please fill all fields")
    return render(request, 'testEntry.html')