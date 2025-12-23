from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from documents.models import Document
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST



def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=name).exists():
            messages.error(request, "Username already exists")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'signup.html')

        User.objects.create_user(username=name, email=email, password=password)
        messages.success(request, "Signup successful! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):
    if request.user.is_authenticated:
        logout(request)

    next_url = request.GET.get('next', '/register/dashboard/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff or user.is_superuser:
                messages.error(request, "Admin users cannot access the user dashboard.")
                return redirect('/register/login/')

            login(request, user)
            return redirect(request.POST.get('next') or next_url)
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html', {'next': next_url})



@login_required(login_url='/register/login/')
def dashboard(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"documents": documents, "user": request.user})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('/register/login/')
