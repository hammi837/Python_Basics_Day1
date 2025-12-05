from django.shortcuts import render , HttpResponse
from homepage.models import Contact
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    context={
         'name':'hammad',
         'course':'Django'
         }
    #return HttpResponse('this is my home page')
    return render(request,'home.html',context)

def about(request):
    #return HttpResponse('this is my about page')
     return render(request,'about.html')


def projects(request):
    #return HttpResponse('this is my projects page')
     return render(request,'projects.html')


def contact(request):
     if request.method=="POST":
          
          name=request.POST['name']
          email=request.POST['email']
          phone=request.POST['phone']
          message=request.POST['message']
          ins= Contact(name=name, email=email, phone=phone, message=message)
          ins.save()
          print('the data has been written to db')

    #return HttpResponse('this is my contact page')
     return render(request,'contact.html')

def services(request):
    #return HttpResponse('this is my services page')
    from django.core.paginator import Paginator
from django.shortcuts import render

def services(request):
    services_list = [
        {"title": "AI & Machine Learning", "desc": "I build AI-powered models and automation solutions."},
        {"title": "Power BI Dashboards", "desc": "Professional dashboards and business insights."},
        {"title": "Django Web Development", "desc": "Backend development, admin panels, and APIs."},
        {"title": "Python Automation", "desc": "Automate reporting, scraping, and workflows."},
        {"title": "Data Analysis", "desc": "Meaningful insights using Python & analytics tools."},
        {"title": "API Development", "desc": "Secure and scalable REST APIs for any project."},
        {"title": "Cloud Solutions", "desc": "Deploy and manage apps in cloud environments."},
        {"title": "SEO Optimization", "desc": "Improve website performance and ranking."},
        # Add more services here
    ]

    # Show 3 services per page
    paginator = Paginator(services_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "services.html", {"page_obj": page_obj})


