from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

#landing page view
def landing(request):
    return render(request, 'core/landing.html')

