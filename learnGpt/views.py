from django.shortcuts import render, redirect, HttpResponse
from user.models import notes
import pdfplumber as pp
import google.generativeai as genai
import os
import dotenv
from django.http import JsonResponse

dotenv.load_dotenv()

def gen(request):
    if request.method == "POST":
        sub = request.POST.get("subject")
        year = request.POST.get("year")
        question = request.POST.get("question")
        pdf_urls = notes.objects.filter(year=year, subject=sub)
        
        extracted_text = ""
        for pdf_note in pdf_urls:
            with pp.open(pdf_note.url.path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    extracted_text += page_text
        
        text = extracted_text
        print(extracted_text)
        api_key = os.getenv("GOOGLE_API_KEY")
        
        try:
            genai.configure(api_key=api_key)
            
            
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(f"Assume you are an expert in the topic of {sub} and you have been asked {question} by a student studying in year {year} of engineering. Answer the question comprehensively with the primary context of notes text: {text}. Also, add additional essential information if necessary, return the text STRICTLY in human understanble language.")
            candidates = getattr(response, 'candidates', [])
            if candidates:
                candidate = candidates[0]
                content = getattr(candidate, 'content', {})
                parts = getattr(content, 'parts', [])
                if parts:
                    generated_text = parts[0].text
                else:
                    generated_text = 'No text parts found in the response'
            else:
                generated_text = 'No candidates found in the response'
            
            """if response.result and response.result.candidates:
                candidate = response.result.candidates[0]
                if candidate.content and candidate.content.parts:
                    generated_text = candidate.content.parts[0].text
                else:
                    generated_text = 'No parts found in the response'
            else:
                generated_text = 'No candidates found in the response'"""
            
            context = {
                'generated_text': generated_text,
                'question': question,
            }
            return JsonResponse(context)
        
        except Exception as e:
            
            return render(request, 'gpt.html', {'error': str(e)})
    
    
    return render(request, "gpt.html")
