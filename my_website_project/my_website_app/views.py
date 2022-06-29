from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def nasa_page(request):
    return render(request, "nasa.html")