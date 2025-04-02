from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/new.html')


def index(request):
    return render(request, 'news/index.html')


def new(request):
    # Ваш код здесь
    return render(request, 'news/new.html')


def about(request):
    return render(request, 'news/about.html')

def contact(request):
       return render(request, 'news/contact.html')


def home(request):
    return render(request, 'home.html')