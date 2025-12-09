from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task, Category 
from django.contrib.auth import logout as auth_logout

  # redirect to login page after logout
 # make sure you have these models


# SIGNUP VIEW
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('name')  # user’s chosen name
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')  # login view name

    return render(request, 'signup.html')


# LOGIN VIEW
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print (username,password)
        user = authenticate(request, username=username, password=password)
        print(username,password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password.")
            

    # For GET request, just render login page
    return render(request, 'login.html')


@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login')

# HOME PAGE VIEW
@login_required
def home(request):
    tasks = Task.objects.filter(owner=request.user)
    categories = Category.objects.all()
    return render(request, 'home.html', {'tasks': tasks, 'categories': categories})




@login_required
def tasks(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'tasks.html', {'tasks': tasks})

# CATEGORIES PAGE
@login_required
def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

#create task
@login_required
def task_create(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        due_date = request.POST.get('due_date')

        category = None
        if category_id:
            category = Category.objects.get(id=category_id)

        Task.objects.create(
            title=title,
            category=category,
            due_date=due_date,
            owner=request.user
        )
        return redirect('tasks')

    return render(request, 'task_create.html', {'categories': categories})

# del task
@login_required
def task_delete(request, id):
    task = Task.objects.get(id=id, owner=request.user)
    task.delete()
    return redirect('tasks')

# create cat
@login_required
def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('categories')

    return render(request, 'category_create.html')

 # del cat
@login_required
def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('categories')



