from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('hi there')
 # return render(request, 'about.html')

def home(request):
    return render(request, 'Home.html')
