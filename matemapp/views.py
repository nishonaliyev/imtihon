from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Fan, Savollar
# Create your views here.

def main(request):
    fan = Fan.objects.all()
    context = {
        'fanlar':fan
    }

    return render(request, 'main.html', context)

def savollar(request, id):
    
    savollar = get_object_or_404(Savollar, id=int(id),)
    savol = Savollar.objects.all()
    context = {
        'savollar':savol
    }

    return render(request, 'savollar.html', context)