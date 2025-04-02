from django.shortcuts import render, redirect


def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')


def home(request):
    return render(request, 'home.html')