from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'password': 'o8cv8dbqh'})


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = request.GET.get('length')
    uppercase = request.GET.get('uppercase')
    numbers = request.GET.get('numbers')
    special = request.GET.get('special')

    if uppercase:
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    if special:
        characters.extend(list('_@#$%^&*'))

    if numbers:
        characters.extend(list('0123456789'))

    print(uppercase,numbers,special)

    generated_pass = ''
    for i in range(int(length)):
        generated_pass += random.choice(characters)

    return render(request, 'generator/password.html',{'pass':generated_pass})

def about(request):
    return render(request,'generator/about.html')