from django.shortcuts import render ,redirect, HttpResponse,get_object_or_404
from .models import*
from django.templatetags.static import static
import os
# user/views.py
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.files.base import ContentFile
import os# Create your views here.
import markdown2

def landing(request):
    doc = docs.objects.all()
    return render(request , "index.html",{"docs":doc})

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
     if request.method =='POST':
         
         sub1 = request.POST.get('subject')
         year = request.POST.get('year')
         sub = sub1.upper()
         if sub and year :
            note = notes.objects.filter(year = year,subject =sub )
     
     return render(request , "notes.html",{"notes":note})
    
     
    #  print(notesa)

def displayDocs(request):
    doc = docs.objects.all()
    return render(request , "index.html",{"docs":doc})

def eventsview(request):
    event_list = events.objects.all()
    
    return render(request,'events.html',{'event_list': event_list})

def eventsinfo(request, event_id):
    event_main = get_object_or_404(events, pk=event_id)
    event_main.description = markdown2.markdown(event_main.description)
    event_details = event.objects.filter(event=event_main)
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

def docreader(request,pk):
    file_link = docs.objects.get(id=pk)
    file_l = file_link.url.name
    filea= os.path.basename(file_l)
    filea = 'docs/'+filea
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

def adddocs(request):
    if request.method == 'POST':
        # Check if files are present in the request
        if 'pdf_files' in request.FILES:
            files = request.FILES.getlist('pdf_files')

            for file in files:
                # Generate a file name and save the file
                file_name = file.name
                file_path = os.path.join(settings.MEDIA_ROOT, 'satic/docs/', file_name)

                # Save file to the media directory
                with default_storage.open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                
                # Save file information in the database
                docs.objects.create(
                    title=file_name[:-4],
                    url=file_path
                )

            return redirect('your_success_url')  # Redirect to a success page or another view

    return render(request, 'upload_pdfs.html')

def upload_pdfs(request):
    if request.method == 'POST':
        # Check if files are present in the request
        if 'pdf_files' in request.FILES:
            files = request.FILES.getlist('pdf_files')

            for file in files:
                # Generate a file name and save the file
                file_name = file.name
                file_path = os.path.join(settings.MEDIA_ROOT, 'satic/roadmaps/', file_name)

                # Save file to the media directory
                with default_storage.open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                
                # Save file information in the database
                roadmaps.objects.create(
                    title=file_name[:-4],
                    url=file_path
                )

            return render('adddocs.html')  # Redirect to a success page or another view

    return render(request, 'adddocs.html')  # Render a template with a file upload form

