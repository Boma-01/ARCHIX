from django.shortcuts import render, redirect
from .models import Meeting
from datetime import datetime
from django.http import JsonResponse


def home(request):

    if request.method == "POST":

        selected_date = request.POST.get("preferred_date")
        selected_time = request.POST.get("preferred_time")

        booking_date = datetime.strptime(selected_date, "%Y-%m-%d").date()

            # Monday = 0
            # Tuesday = 1
            # Wednesday = 2
            # Thursday = 3
            # Friday = 4
            # Saturday = 5
            # Sunday = 6

        if booking_date.weekday() >= 5:
            return JsonResponse({
                "success": False,
                "message": "Consultations are only available Monday to Friday."
            })

        meeting_exists = Meeting.objects.filter(
            preferred_date=selected_date,
            preferred_time=selected_time
        ).exists()

        if meeting_exists:

            return JsonResponse({
                "success": False,
                "message": "Sorry, this time slot has already been booked."
            })

        Meeting.objects.create(

            full_name=request.POST.get("full_name"),

            email=request.POST.get("email"),

            phone=request.POST.get("phone"),

            project_type=request.POST.get("project_type"),

            preferred_date=selected_date,

            preferred_time=selected_time,
            
            project_description=request.POST.get("project_description")

        )

        return JsonResponse({
            "success": True,
            "message": "Consultation booked successfully!"
        })

    return render(request, "main/Index.html")

def about(request):
    return render(request, "main/About.html")


def projects(request):
    return render(request, "main/project.html")


def services(request):
    return render(request, "main/service.html")


def contact(request):
    return render(request, "main/contact.html")