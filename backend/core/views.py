from django.shortcuts import render
import datetime
from django.contrib import messages
# from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate ,login , logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from channels.auth import login , logout
from core.EmailBackEnd import EmailBackEnd

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