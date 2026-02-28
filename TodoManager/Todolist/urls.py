from django.urls import path, include
from Todolist import views

urlpatterns = [
    path('', views.home, name="home"),
    path('todolist/', views.Todolist, name="todolist"),
    path('todolist/edit_task/<task_id>/', views.edit_task, name="edit_task"),
    path('todolist/delete_task/<task_id>/', views.delete_task, name="delete_task"),
    path('todolist/complete/<task_id>/', views.complete_task, name="complete_task"),
    path('todolist/pending/<task_id>/', views.pending_task, name="pending_task"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),    
]