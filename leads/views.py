from django.shortcuts import render
#from django.http import HttpResponse
from .models import Lead

def home_page(request):
   # return HttpResponse("Hello world!!")
   """ context = {
      "name": "joe",
      "age": 35
   } """

   leads = Lead.objects.all()
   context = {
      "leads": leads
   }
   return render(request, "second_page.html", context)
