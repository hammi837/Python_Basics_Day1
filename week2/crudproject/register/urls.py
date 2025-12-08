from django.urls import path 
from register import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('contacts/',views.contacts,name='contacts')

    
]