from django.shortcuts import render
import datetime
from django.contrib import messages
# from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate ,login , logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from channels.auth import login , logout
from core.EmailBackEnd import EmailBackEnd
from .models import Employer, CustomUser, Applicant

def admin_home(request):
    return render(request, 'home_content.html')


def showDemoPage(request):
    return render(request, 'demo.html')


def ShowLoginPage(request):
    return render(request, 'login_page.html')

#form data passing on form submit else error
def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2 > Method Not Allowed </h2> ")
    else:
        user = EmailBackEnd.authenticate(request, username = request.POST.get("email"), password = request.POST.get("password"))
        if user != None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect('/admin_home')
            else:
                return HttpResponse("Student Login"+str(user.user_type))
            # return HttpResponse("Email :" + request.POST.get("email") + "Password :" + request.POST.get("password"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")


def add_employer(request):
    courses = Employer.objects.all()
    return render(request, 'employer_template/add_employer_template.html',{"courses":courses})



def add_employer_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allow")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email, user_type=3)
            user.employer.address = address
            user.save()
            messages.success(request, "Successfully added employer")
            return HttpResponseRedirect("/add_employer")
        except:
            messages.error(request, "Failed to add employer")
            return HttpResponseRedirect("/add_employer")
