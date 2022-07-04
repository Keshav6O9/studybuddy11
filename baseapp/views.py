from django.shortcuts import redirect, render
from baseapp.models import *
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
import random
import string
from django.contrib.auth.models import User, auth
# Create your views here.
characters = string.ascii_letters + string.digits + string.punctuation
userName = ''.join(random.choice(characters) for i in range(3))
def home(request):
    return render(request, 'home.html')
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render())
def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        exams = request.POST.get('exams')
        passwordmain = request.POST.get('password')
        confirmPassword = request.POST.get('password1')
        password = ""
        print("pass1",passwordmain)
        print("pass2",confirmPassword)
        if passwordmain == confirmPassword:
            password += passwordmain
            print("passwordd:",password)
        
        username = request.POST.get('username')
        data = user(firstName=first_name, lastName=last_name,username=username,
                      mobile=mobile, email=email,passwordHash=password,exams=exams)
        userr = User.objects.create_user(first_name=first_name, last_name=last_name,username=username,
                      email=email,password=password)
        userr.save()
        data.save()
    return render(request, 'registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        print("username",username)
        print('password',password)

        if user is not None:
         auth.login(request,user)
         return redirect("index.html")
        else:
             print("invalid credentials")
             return redirect('login.html')
    else:
     return render(request,'login.html')

