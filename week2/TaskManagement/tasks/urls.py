from django.urls import path
from tasks import views

urlpatterns = [
 
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
   path('logout/', views.logout_view, name='logout_view'),
    path('', views.home, name='home'),

    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/delete/<int:id>/', views.task_delete, name='task_delete'),

    path('categories/', views.categories, name='categories'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/delete/<int:id>/', views.category_delete, name='category_delete'),
]


