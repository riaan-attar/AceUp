from django.shortcuts import render , render , redirect, HttpResponse
from user.models import notes
import pdfplumber as pp

def gen(request):
    if request.method == "POST":
        sub = request.POST.get("subject")
        year = request.post.get("year")
        question = request.POST.get("question")
        pdf_urls = notes.objects.filter(year =year,subject = sub)
        extracted_text =""
        for pdf_path  in pdf_urls:
            with pp.open(pdf_path) as pdf:
                for page in pdf.pages:
                    # Extract text from each page
                    page_text = page.extract_text()
                    extracted_text += page_text
        

