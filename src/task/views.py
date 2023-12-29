from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout, authenticate 
from .models import Task
from .forms import TaskForm

@login_required
def home_view(request):
    tasks = Task.objects.all()
    states = ['TO DO','WAITING','IN PROGRESS','DONE']
    context = {'tasks': tasks, 'states': states}
    return render(request, 'home.html', context)

@method_decorator(login_required, name='dispatch')
class ListTasksView(View):
    template_name = 'task_list.html'

    def get(self, request):
        tasks = Task.objects.filter(assigned_to=request.user)
        return render(request, self.template_name, {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_to = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

""" def login_view(request):
    context={}
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        print("username ",username)
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
        
    else:
        context = {'message': "Your username and password didn't match. Please try again."}
    return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login') 
 """