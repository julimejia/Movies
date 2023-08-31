from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Movie



def home (request):  
   searchTerm = request.GET.get('searchMovie')
   if searchTerm:
      mov = Movie.objects.filter(title__icontains=searchTerm)
   else: 
      mov = Movie.objects.all()
   return render(request, 'home.html', {'movies': mov,})

def about(request):  
   return render(request, 'about.html')

