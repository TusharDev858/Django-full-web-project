from datetime import datetime
from multiprocessing import context
import django
from django.shortcuts import render, redirect
from Todolist.models import Contact, Task
from Todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



def home(request):
    context = {
        'page': 'Home page'
    }
    return render(request, "main.html", context)

@login_required
def Todolist(request):
    if request.method == 'POST':
        form_data = TaskForm(request.POST or None)
        if form_data.is_valid():
            instance = form_data.save(commit=False)
            instance.owner = request.user
            instance.save()
            messages.success(request, "Task added successfully!")
            return redirect('todolist')
        else:
            messages.error(request, "Form is not valid!")
        
    all_tasks = Task.objects.filter(owner=request.user)
    paginator = Paginator(all_tasks, 10)
    page = request.GET.get('page')
    
    all_tasks = paginator.get_page(page)
    
    context = {
        'page': 'Todolist page',
        'all_tasks': all_tasks
    }
    return render(request, "Todolist.html", context)

@login_required
def delete_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    if task_obj.owner == request.user:
        task_obj.delete()
        messages.success(request, f"Task - {task_obj.task} deleted successfully!")
    else:
        messages.error(request, "Task cannot be deleted by you!")
    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    context = {
        'task_obj': task_obj
    }
    if request.method == 'POST':
        form_data = TaskForm(request.POST, instance=task_obj)
        if form_data.is_valid():            
            form_data.save()
            messages.success(request, "Task updated successfully!")
            return redirect('todolist')
        else:
            messages.error(request, "Form is not valid!")
    return render(request, "edit.html", context)

@login_required
def complete_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    if task_obj.owner == request.user:
        task_obj.is_completed = True
        task_obj.save()
        messages.success(request, "status changed")
    else:
        messages.error(request, "Task cannot be changed by you!")
    
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    if task_obj.owner == request.user:
        task_obj.is_completed = False
        task_obj.save()
        messages.success(request, "status changed")
    else:
        messages.error(request, "Task cannot be changed by you!")
    return redirect('todolist')
    
def about(request):
    context = {
        'page': 'About section'
    }
    return render(request, "about.html", context)



# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         desc = request.POST.get('desc')

#         contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
#         contact.save()
#         messages.success(request, "Your message has been sent!")

#     return render(request, 'contact.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        desc = request.POST.get('desc', '').strip()

        if name and email and phone and desc:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, "Your message has been sent!")
            return redirect('contact')  # Redirect or render the same page to clear the form
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, 'contact.html')
