from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.views.generic import CreateView
from django.views.generic import TemplateView
from .forms import *
from .models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("register")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/signup.html", context={"register_form":form})


#@method_decorator([ applicant_required],name='dispatch')
class ApplicantSignUpView(CreateView):
    model = User
    form_class = ApplicantSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'applicant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

#@method_decorator([employer_required],name='dispatch')
class EmployerSignUpView(CreateView):
    model = User
    form_class = EmployerSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class SignUpView(TemplateView):
    template_name = 'registration/signup_form.html'

def home(request):
    return render(request,'myapp/appdash.html')


def index(request):
    return render(request,'myapp/empdash.html')