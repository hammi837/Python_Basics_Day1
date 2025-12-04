from django.shortcuts import render , HttpResponse
from homepage.models import Contact

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
