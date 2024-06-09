from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .froms import TaskForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from apps.projects.models import ProjectMember



# Create your views here.
@login_required
def view_tasks(request,project_version_id):
    if project_version_id==0:
        #este es para ver mis tareas en todos los proyectos
        menbers=ProjectMember.objects.filter(user=request.user).values_list('id', flat=True)
        tasks=Task.objects.filter(completed=False,assigned_to_id__in=menbers).order_by('-created_at')
    else:
        #para ver las tareas de un proyecto
        menbers=ProjectMember.objects.filter(user=request.user).values_list('id', flat=True)
        tasks=Task.objects.filter(project_version_id=project_version_id,completed=False,assigned_to_id__in=menbers).order_by('-created_at')
    return render(request, 'tasks/view_tasks.html', {
        'tasks':tasks,
        'task_view_type':'View pending tasks'
        })

@login_required
def view_all_tasks(request,project_version_id):
    if project_version_id==0:
        menbers=ProjectMember.objects.filter(user=request.user).values_list('id', flat=True)
        tasks=Task.objects.filter(assigned_to_id__in=menbers).order_by('-created_at')
    else:
        menbers=ProjectMember.objects.filter(user=request.user).values_list('id', flat=True)
        tasks=Task.objects.filter(project_version_id=project_version_id,assigned_to_id__in=menbers).order_by('-created_at')
    return render(request, 'tasks/view_tasks.html', {
        'tasks':tasks,
        'task_view_type':'View all tasks'
        })


@login_required
def view_completed_tasks(request,project_version_id):
    if project_version_id==0:
        #este es para ver mis tareas en todos los proyectos
        menbers=ProjectMember.objects.filter(user=request.user).values_list('id', flat=True)
        tasks=Task.objects.filter(completed=True,assigned_to_id__in=menbers).order_by('-created_at')
    else:
        #para ver las tareas de un proyecto
        menbers=ProjectMember.objects.filter(user=request.user).values_list('id', flat=True)
        tasks=Task.objects.filter(project_version_id=project_version_id,completed=True,assigned_to_id__in=menbers).order_by('-created_at')
    return render(request, 'tasks/view_tasks.html', {
        'tasks':tasks,
        'task_view_type':'View complete tasks'
        })

@login_required
def create_task(request):
    if request.method == 'POST':
        try:
            form = TaskForm(request.POST,user=request.user)
            # form.project_version=project_version_id
            newtask = form.save()
            newtask.save()
            return redirect('view_tasks',0)
        except ValueError:
            return render(request,'tasks/create_task.html',{
            'form':form,
            'error':'ingresa datos validos'
            })
    else:
        form = TaskForm(user=request.user)
        return render(request, 'tasks/create_task.html', {'form':form})
    

@login_required
def manage_task(request,taks_id):
    if request.method=='GET':
        if taks_id==0:
            menbers=ProjectMember.objects.filter(user=request.user).values_list('id', flat=True)
            tasks=Task.objects.filter(completed=False,assigned_to_id__in=menbers).order_by('-created_at')
            return render(request,"select_tasks/select_pages.html",{
                'tasks':tasks,
                'redirect_funcion':'manage_task',

            })
        else:
            menbers=ProjectMember.objects.filter(user=request.user).values_list('id', flat=True)
            task=get_object_or_404(Task,pk=taks_id,assigned_to_id__in=menbers)
            form = TaskForm(instance=task)
            return render(request,'tasks/manage_task.html',
            {
                'task':task,
                'form':form
            })
        

@login_required
def update_task(request,taks_id):
    try:
        tasks=get_object_or_404(Task,pk=taks_id)
        form = TaskForm(request.POST,instance=tasks)
        form.save()
        return redirect('view_tasks',0)
    except ValueError:
        return render(request,'tasks/manage_task.html',
        {
            'tasks':tasks,  
            'form':form,
            'error':'error actualizar tareas'
        })


@login_required
def complete_task(request,taks_id):
    # project=get_object_or_404(Project,pk=project_id,user=request.user)
    tasks=get_object_or_404(Task,pk=taks_id)
    if request.method =='POST':
        tasks.completed=True
        tasks.completed_at=timezone.now()
        tasks.save()
        return redirect('view_tasks', 0)
    

@login_required
def delete_task(request,taks_id):
    tasks=get_object_or_404(Task,pk=taks_id)
    if request.method =='POST':
        tasks.delete()
        return redirect('view_tasks', 0)
    
