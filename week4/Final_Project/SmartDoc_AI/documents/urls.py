from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('upload/', views.upload, name='upload'),
    path("<int:doc_id>/ask/", views.ask_ai, name="ask_ai"),
]
