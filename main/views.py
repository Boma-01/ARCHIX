from django.shortcuts import render, redirect
from .models import Meeting


def home(request):

    if request.method == "POST":

        Meeting.objects.create(

            full_name=request.POST.get("full_name"),

            email=request.POST.get("email"),

            phone=request.POST.get("phone"),

            project_type=request.POST.get("project_type"),

            preferred_date=request.POST.get("preferred_date"),

            preferred_time=request.POST.get("preferred_time"),

            project_description=request.POST.get("project_description")

        )

        return redirect("home")

    return render(request, "main/Index.html")


def about(request):
    return render(request, "main/About.html")


def projects(request):
    return render(request, "main/project.html")


def services(request):
    return render(request, "main/service.html")


def contact(request):
    return render(request, "main/contact.html")