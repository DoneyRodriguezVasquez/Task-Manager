from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.db.models import Count
from .models import Task, Project
from .forms import TaskForm, ProjectForm

@login_required
def home_view(request):
    if request.method == 'GET':
        if request.GET.get('value') == 'dragged':
            task = get_object_or_404(Task, id=request.GET.get('id'))
            task.state = request.GET.get('state')
            task.save()
    states = {'TO_DO':'TO DO','WAITING':'WAITING','IN_PROGRESS':'IN PROGRESS','DONE':'DONE'}
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'states': states }
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
    titulo = "Crear tarea"
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_to = request.user
            task.save()
            return redirect('task:home')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form, 'titulo': titulo})

@login_required
def edit_task(request, task_id):
    titulo = "Editar tarea"
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'create_task.html', {'form': form, 'task': task, 'titulo': titulo})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect("task:home")
    else:
        form = TaskForm(instance=task)
    return render(request, 'delete_task.html', {'form': form, 'task': task})

@login_required  
def config(request):
    project = Project.objects.all()
    User = get_user_model()
    users = User.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()

    form = ProjectForm()
    authForm = UserCreationForm()
    return render(request, 'config.html', {'form': form, 'authForm':authForm, 'project':project, 'users':users})

@login_required 
def report(request):
    # Obtener el recuento de tareas por estado
    datos_reporte = Task.objects.values('state').annotate(total=Count('state'))

    # Preparar datos para gráfico de barras
    labels = [dato['state'] for dato in datos_reporte]
    valores = [dato['total'] for dato in datos_reporte]

    return render(request, 'report.html' , {'labels': labels, 'valores': valores})

def logout_view(request):
    logout(request)
    return redirect("task:home") 