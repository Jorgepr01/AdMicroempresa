from django.shortcuts import render,get_object_or_404,redirect
from .forms import FormTeam, FormTeamMember
from .models import Team, TeamMember


# Create your views here.
def view_teams(request):
    teams = Team.objects.all()
    print(teams[0])
    return render(request, 'team/view_teams.html', {'teams':teams})



def create_team(request):
    if request.method == 'GET':
        return render(request, 'team/create_team.html', {
            'form': FormTeam
        })
    else:
        try:
            form = FormTeam(request.POST)
            newtasks = form.save()
            # newtasks.user= request.user
            newtasks.save()
            return redirect('teams')
        except ValueError:
            return render(request,"team/create_team.html",{
            'form':FormTeam,
            'error':'ingresa datos validos'
            })

def manage_team(request):
    return render(request, 'manage_team.html')



def manage_team(request,team_id):
    if request.method=='GET':
        if team_id==0:
            teams=Team.objects.all()
            return render(request,"selects/select_pages.html",{
                'teams':teams,
                'redirect_funcion':'manage_team',

            })
        else:
            team=get_object_or_404(Team,pk=team_id)
            form = FormTeam(instance=team)
            return render(request,'team/manage_team.html',
            {
                'team':team,
                'form':form
            })
    

#API para actualizar la tarea

def update_team(request,team_id):
    try:
        team=get_object_or_404(Team,pk=team_id)
        form = FormTeam(request.POST,instance=team)
        form.save()
        print(request.POST)
        return redirect('teams')
    except ValueError:
        return render(request,'team/manage_team.html',
        {
            'team':team,
            'form':form,
            'error':'error actualizar tareas'
        })


#API para eliminar la tarea

def delete_team(request,team_id):
    project=get_object_or_404(Team,pk=team_id)
    if request.method =='POST':
        project.delete()
        return redirect('teams')







def view_menbers_team(request,team_id):
    if request.method == 'GET':
        if team_id==0:
            teams=Team.objects.all()
            return render(request,"selects/select_pages.html",{
                'teams':teams,
                'redirect_funcion':'view_menbers_team',
            })
        else:
            team=get_object_or_404(Team,pk=team_id)
            members=TeamMember.objects.filter(team_id=team_id)
            return render(request,'member_team/view_members_team.html',{'team':team,'members':members})
        

    
def create_members_team(request,team_id):
    if request.method == 'GET':
        if team_id==0:
            teams=Team.objects.all()
            return render(request,"selects/select_pages.html",{
                'teams':teams,
                'redirect_funcion':'create_members_team',
            })
        else:
            return render(request, 'member_team/create_members_team.html', {
                'form': FormTeamMember,
                'team_id':team_id
            })

    else:
        try:
            form = FormTeamMember(request.POST)
            newmember = form.save()
            # team=get_object_or_404(Team,pk=team_id)
            # newmember.team=team
            newmember.save()
            return redirect('view_menbers_team',team_id)
        except ValueError:
            return render(request,"member_team/create_members_team.html",{
            'form':FormTeamMember,
            'error':'ingresa datos validos'
            })



def manage_members_team(request,team_id,member_id):
    if request.method == 'GET':
        if team_id==0:
            teams=Team.objects.all()
            return render(request,"selects/select_pages.html",{
                'teams':teams,
                'redirect_funcion':'manage_members_team',
            })
        else:
            team=get_object_or_404(Team,pk=team_id)
            member=get_object_or_404(TeamMember,pk=member_id)
            form = FormTeamMember(instance=member)
            return render(request,'member_team/manage_members_team.html',
            {
                'team':team,
                'member':member,
                'form':form
            })

def update_members_team(request,team_id,member_id):
    try:
        team=get_object_or_404(Team,pk=team_id)
        member=get_object_or_404(TeamMember,pk=member_id)
        form = FormTeamMember(request.POST,instance=member)
        form.save()
        print(request.POST)
        return redirect('view_menbers_team',team_id)
    except ValueError:
        return render(request,'member_team/manage_members_team.html',
        {
            'team':team,
            'member':member,
            'form':form,
            'error':'error actualizar miembros'
        })
    


def delete_members_team(request,team_id,member_id):
    if request.method == 'POST':
        member=get_object_or_404(TeamMember,pk=member_id,team_id=team_id)
        member.delete()
        return redirect('view_menbers_team',team_id)