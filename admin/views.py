from django.shortcuts import render ,redirect,HttpResponse
from user.models import * 
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.files.base import ContentFile
import os
from .forms import *
from django.forms import formset_factory
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

            return redirect('your_success_url')  # Redirect to a success page or another view

    return render(request, 'upload_pdfs.html')  # Render a template with a file upload form

def noteEntry(request):
    if request.method == 'POST':
        # Check if files are present in the request
        if 'pdf_files' in request.FILES:
            files = request.FILES.getlist('pdf_files')
            subject = request.POST.get("subject")
            year = request.POST.get("year")
            for file in files:
                # Generate a file name and save the file
                file_name = file.name
                file_path = os.path.join(settings.MEDIA_ROOT, 'satic/notes/', file_name)

                # Save file to the media directory
                with default_storage.open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                
                # Save file information in the database
                notes.objects.create(
                    title=file_name[:-4].upper(),
                    url=file_path,
                    subject = subject.upper(),
                    year=year
                )
        else:
            return HttpResponse("Please fill all fields")
    return render(request, 'noteEntry.html')


# Create your views here.
# def noteEntry(request):
#     if request.method == "POST" :
#         title = request.POST.get("title")
#         year = request.POST.get("year")
#         subject = request.POST.get("subject")
#         url = request.FILES.get("url")
#         unit = request.POST.get("unit")
#         if title and subject and year and url and unit :
#             n = notes.objects.create (
#             title = title,
#             year = year,
#             subject = subject,
#             url = url, 
#             unit = unit)
#             n.save()
#         else:
#             return HttpResponse("Please fill all fields")
#     return render(request, 'noteEntry.html')

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



def event_upload(request):
    EventFormSet = formset_factory(EventForm, extra=1, can_delete=True)
    
    if request.method == 'POST':
        events_form = EventsForm(request.POST, request.FILES)
        formset = EventFormSet(request.POST, request.FILES)
        
        if events_form.is_valid() and formset.is_valid():
            # Save the events instance
            event_instance = events_form.save()
            
            # Save each event form in the formset
            for form in formset:
                if form.cleaned_data and form.cleaned_data.get('photos'):
                    event_instance_form = form.save(commit=False)
                    event_instance_form.event = event_instance
                    event_instance_form.save()
            
            return redirect('event_list')
    else:
        events_form = EventsForm()
        formset = EventFormSet()
    
    return render(request, 'test1.html', {
        'events_form': events_form,
        'formset': formset
    })