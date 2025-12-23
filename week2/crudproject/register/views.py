from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signup(request):
 if request.method=='POST':
     name=request.POST.get('name')
     email=request.POST.get('email')
     password=request.POST.get('password')
     print(name, email, password)
     myuser=User.objects.create_user(name, email, password)
     myuser.save()
     return redirect("login")


 return render(request, 'signup.html')
    
def login(request):
    if request.method=='POST':
       email=request.POST.get('email')
       password=request.POST.get('password')
       myuser=authenticate(username='email', password='password')
       if myuser is not None:
          login(request,myuser)
          return redirect('contacts')
       else:
            messages.error(request, "Invalid email or password.")
       
    return render(request,'login.html')
 

@login_required
def contacts(request):
   return render(request,'contacts.html')
   

    
