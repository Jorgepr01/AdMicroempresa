from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.projects.froms import formProjects,formProjectVersions,ProyectoFormSet,FormProjectMember
from apps.projects.models import Project,ProjectVersion,ProjectMember
from django.utils import timezone


# Create your views here.

def index(request):
    return render(request, 'index.html')



# def create_projects(response):
#     if response.method=='GET':
#         return render(response, "projects/create_project.html",{
#         "form":formProjects(),
#         })
#     else:
#         titulo=(response.POST["title"])
#         des=(response.POST["description"])
#         spr=(response.POST["startproject"])
#         endpr=(response.POST["endproject"])
#         Project.objects.create(name=titulo,description=des,start_date=spr,end_date=endpr,)
#         return redirect("view_project")


def create_projects(request):
    if request.method == 'GET':
        return render(request, 'project/create_project.html', {
            'form': formProjects
        })
    else:
        try:
            form = formProjects(request.POST)
            newtasks = form.save()
            # newtasks.user= request.user
            newtasks.save()
            return redirect('view_project')
        except ValueError:
            return render(request,"project/create_project.html",{
            'form':formProjects,
            'error':'ingresa datos validos'
            })

    
@login_required
def view_project(request):
    project=Project.objects.all()
    return render(request, 'project/view_project.html',{'project':project})

def manage_project(request,project_id):
    if request.method=='GET':
        if project_id==0:
            projects=Project.objects.all()
            return render(request,"select_pages.html",{
                'projects':projects,
                'redirect_funcion':'manage_project',
                'seleccion':'project',

            })
        else:
            project=get_object_or_404(Project,pk=project_id)
            form = formProjects(instance=project)
            return render(request,'project/manage_project.html',
            {
                'project':project,
                'form':form
            })
    

#API para actualizar la tarea

def update_project(request,project_id):
    try:
        project=get_object_or_404(Project,pk=project_id)
        form = formProjects(request.POST,instance=project)
        form.save()
        print(request.POST)
        return redirect('view_project')
    except ValueError:
        return render(request,'project/manage_project.html',
        {
            'project':project,
            'form':form,
            'error':'error actualizar tareas'
        })

    
def complete_project(request,project_id):
    # project=get_object_or_404(Project,pk=project_id,user=request.user)
    project=get_object_or_404(Project,pk=project_id)
    if request.method =='POST':
        project.datecompleted=timezone.now()
        project.save()
        return redirect('view_project')



#API para eliminar la tarea

def delete_project(request,project_id):
    project=get_object_or_404(Project,pk=project_id)
    if request.method =='POST':
        project.delete()
        return redirect('view_project')


def view_project_versions(request,project_id):
    if request.method=='GET':
        if project_id==0:
            projects=Project.objects.all()
            return render(request,"select_pages.html",{
                'projects':projects,
                'redirect_funcion':'view_project_versions',
                'seleccion':'project',
            })
        else:
            project=get_object_or_404(Project,pk=project_id)
            versions = ProjectVersion.objects.filter(project_id=project_id)
            print(project)
            print(versions)
            return render(request,'project_version/view_project_versions.html',{
                'project':project,
                'versions':versions
                })
        
def create_project_version(request,project_id):
    if request.method=='GET':
        if project_id==0:
            projects=Project.objects.all()
            return render(request,"select_pages.html",{
                'projects':projects,
                'redirect_funcion':'create_project_version',
                'seleccion':'project',
            })
        else:
            return render(request, 'project_version/create_project_version.html', {
                'form': formProjectVersions,
                'project_id':project_id
            })

    else:
        try:
            form = formProjectVersions(request.POST)
            newversion = form.save()
            newversion.project=get_object_or_404(Project,pk=project_id)
            newversion.save()
            return redirect('view_project_versions',project_id)
        except ValueError:
            return render(request,"project_version/create_project_version.html",{
            'form':formProjectVersions,
            'error':'ingresa datos validos'
            })






def manage_project_version(request,project_id,project_version_id):
    if request.method=='GET':
        project_version=get_object_or_404(ProjectVersion,pk=project_version_id,project=project_id)
        form = formProjectVersions(instance=project_version)
        return render(request,'project_version/manage_project_version.html',
        {
            'project_version':project_version,
            'form':form
        })
    




#API para actualizar la tarea

def update_project_version(request,project_id,project_version_id):
    try:
        project_version=get_object_or_404(ProjectVersion,pk=project_version_id,project_id=project_id)
        form = formProjectVersions(request.POST,instance=project_version)
        form.save()
        print(request.POST)
        return redirect('view_project_versions',project_id)
    except ValueError:
        return render(request,'project_version/manage_project_version.html',
        {
            'project':project_version,
            'form':form,
            'error':'error actualizar tareas'
        })

    
#API para eliminar la tarea

def delete_project_version(request,project_id,project_version_id):
    project_version=get_object_or_404(ProjectVersion,pk=project_version_id,project_id=project_version_id)
    if request.method =='POST':
        project_version.delete()
        return redirect('view_project_versions',project_id)




# crear los members del proyecto

def view_menbers_project(request,project_id):
    if request.method == 'GET':
        if project_id==0:
            projects=Project.objects.all()
            return render(request,"select_pages.html",{
                'projects':projects,
                'redirect_funcion':'view_menbers_project',
                'seleccion':'project',
            })
        else:
            project=get_object_or_404(Project,pk=project_id)
            members=ProjectMember.objects.filter(project_id=project_id)
            return render(request,'member_project/view_members_project.html',{'project':project,'members':members})







def create_members_project(request,project_id):
    if request.method == 'GET':
        if project_id==0:
            projects=Project.objects.all()
            return render(request,"select_pages.html",{
                'projects':projects,
                'redirect_funcion':'create_members_project',
                'seleccion':'project',
            })
        else:
            return render(request, 'member_project/create_members_project.html', {
                'form': FormProjectMember,
                'team_id':project_id
            })
    else:
        try:
            form = FormProjectMember(request.POST)
            newmember = form.save()
            # team=get_object_or_404(Team,pk=team_id)
            # newmember.team=team
            newmember.save()
            return redirect('view_menbers_project',project_id)
        except ValueError:
            return render(request,"member_project/create_members_project.html",{
            'form':FormProjectMember,
            'error':'ingresa datos validos'
            })


def manage_members_project(request,project_id,member_id):
    if request.method == 'GET':
        if project_id==0:
            projects=Project.objects.all()
            return render(request,"view_menbers_project",{
                'projects':projects,
                'redirect_funcion':'manage_members_project',
            })
        else:
            project=get_object_or_404(Project,pk=project_id)
            member=get_object_or_404(ProjectMember,pk=member_id)
            form = FormProjectMember(instance=member)
            return render(request,'member_project/manage_members_project.html',
            {
                'project':project,
                'member':member,
                'form':form
            })
        