from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .froms import TaskForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone



# Create your views here.
@login_required
def view_tasks(request):
    tasks=Task.objects.all()
    return render(request, 'tasks/view_tasks.html', {'tasks':tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        try:
            form = TaskForm(request.POST)
            # form.project_version=project_version_id
            newtask = form.save()
            newtask.save()
            return redirect('view_tasks')
        except ValueError:
            return render(request,'tasks/create_task.html',{
            'form':form,
            'error':'ingresa datos validos'
            })
    else:
        return render(request, 'tasks/create_task.html', {'form':TaskForm})
    

@login_required
def manage_task(request,taks_id):
    if request.method=='GET':
        if taks_id==0:
            tasks=Task.objects.all()
            return render(request,"select_tasks/select_pages.html",{
                'tasks':tasks,
                'redirect_funcion':'manage_task',

            })
        else:
            task=get_object_or_404(Task,pk=taks_id)
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
        print(request.POST)
        return redirect('view_tasks')
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
        return redirect('view_tasks')
    

@login_required
def delete_task(request,taks_id):
    tasks=get_object_or_404(Task,pk=taks_id)
    if request.method =='POST':
        tasks.delete()
        return redirect('view_tasks')