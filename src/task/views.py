from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.db.models import Count
from .models import Task, Project
from .forms import TaskForm, ProjectForm
from datetime import datetime
from datetime import timedelta


def set_messages(request):
    five_days = datetime.now() + timedelta(days=5)
    overdue_tasks = Task.objects.filter(status__in =['TO_DO','IN_PROGRESS'], date__lte= datetime.now()).count()
    messages.error(request,'Tareas expiradas: '+ str(overdue_tasks))
    print("tareas expiradas: ", overdue_tasks)
    tasks_expiring = Task.objects.filter(status__in =['TO_DO','IN_PROGRESS'], date__range = (datetime.now(), five_days)).count()
    print("tareas por vencer: ", tasks_expiring)
    messages.warning(request,'Tareas a punto de vencer: '+str(tasks_expiring))




@login_required
def home_view(request):
    return render(request, 'home.html')

#funcion para listar las tareas en la ventana principal, tiene filtros y opciones para el cambio de estado de las tareas. 
@login_required
def task_list(request):
    status = {'TO_DO':'TO DO','IN_PROGRESS':'IN PROGRESS','DONE':'DONE'}
    task = ''
    projects = ''
    set_messages(request)

    if request.method == 'GET':
        #actualiza el estado de la tarea cuando se mueve de columna o cuando en la ventana modal se cambia de estado la tarea
        if request.GET.get('value') in ['dragged', 'changed']:
            task = get_object_or_404(Task, id=request.GET.get('id'))
            task.status = request.GET.get('status')
            task.save()
        #filtra las tareas por usuario o por projecto.
        elif request.GET.get('value') == 'filtered':  
           
            filter_type = request.GET.get('filter_type')
            filter_value = request.GET.get('filter_value')
           
            if filter_type == 'filter_user':
                tasks = Task.objects.filter(assigned_to=filter_value).order_by('priority','date') 
            elif filter_type == 'filter_project':
                tasks = Task.objects.filter(project__id=filter_value).order_by('priority','date') 
            else:
                tasks = Task.objects.all().order_by('priority','date')
            projects = Project.objects.all()
            context = {'tasks': tasks, 'status': status, 'projects': projects}
            return render(request, 'task/list_task.html', context)
    
    tasks = Task.objects.all().order_by('priority','date') 
    projects = Project.objects.all()
    context = {'tasks': tasks, 'status': status, 'projects': projects }
    return render(request, 'task/list_task.html', context)

@method_decorator(login_required, name='dispatch') 
class ListTasksView(View):
    template_name = 'task/task_list.html'

    def get(self, request):
        tasks = Task.objects.filter(assigned_to=request.user)
        return render(request, self.template_name, {'tasks': tasks})

@login_required
def create_task(request):
    titulo = "Crear tarea"
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_to = request.user
            task.save()
            messages.success(request,'Tarea creada')
            return redirect('task:task_list')
    else:
        form = TaskForm()
    return render(request, 'task/create_task.html', {'form': form, 'titulo': titulo})

@login_required
def edit_task(request, task_id):
    titulo = "Editar tarea"
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,'Tarea actualizada')
            return redirect('task:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/create_task.html', {'form': form, 'task': task, 'titulo': titulo})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        messages.success(request,'Tarea borrada')
        return redirect("task:task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/delete_task.html', {'form': form, 'task': task})

@login_required  
def config(request):
    project = Project.objects.all()
    User = get_user_model()
    users = User.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Proyecto creado')

    form = ProjectForm()
    authForm = UserCreationForm()
    return render(request, 'task/config.html', {'form': form, 'authForm':authForm, 'project':project, 'users':users})

@login_required  
def del_project(request, id):
    project = get_object_or_404(Project, pk=id)
    if request.method == 'POST':
        project.delete()
        messages.success(request,'Projecto borrado')
        return redirect("task:config")
    else:
        form = ProjectForm(instance=project)
    return render(request, 'task/delete_project.html', {'form': form, 'project':project})


@login_required 
def report(request):
    # Obtener el recuento de tareas por estado
    datos_reporte = Task.objects.values('status').annotate(total=Count('status'))

    # Preparar datos para gráfico de barras
    labels = [dato['status'] for dato in datos_reporte]
    valores = [dato['total'] for dato in datos_reporte]

    return render(request, 'task/report.html' , {'labels': labels, 'valores': valores})

def logout_view(request):
    logout(request)
    return redirect("task:home") 