from django.shortcuts import render

def home(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def projects(request):
    return render(request, "main/project.html")

def services(request):
    return render(request, "main/service.html")

def contact(request):
    return render(request, "main/contact.html")