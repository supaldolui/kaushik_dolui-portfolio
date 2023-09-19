from django.shortcuts import render
from portfolio.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse

def index(request):
    skills = SkillCard.objects.all() 
    projects = ProjectCard.objects.all()
    context = {
        'skills': skills,
        'projects': projects,
    }
    return render(request, 'base.html',context)


def send_contact_email(request):
    if request.method == "POST":
        # Get the form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save the submission to the database
        submission = ContactSubmission(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        submission.save()
        send_mail("THANKS FOR VISITING MY PORTFOLIO: ",f"Hey {name} I recieved yours message , thanks for that!!!",settings.EMAIL_HOST_USER,[email],fail_silently=True)

        # Compose and send the email (your existing code)

        return render(request, 'base.html')
    else:
        print("something went wrong")
        return HttpResponse("Invalid request method.")
