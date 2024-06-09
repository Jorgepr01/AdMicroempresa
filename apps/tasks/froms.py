from django import forms
from .models import Task
from apps.projects.models import ProjectMember,ProjectVersion
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = ['name', 'description', 'assigned_to', 'status', 'priority', 'due_date']
        fields = ['name','project_version', 'description', 'assigned_to', 'status', 'priority', 'due_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'project_version': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Project Version'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 4}),
            'assigned_to': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Assigned To'}),
            'status': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Status'}),
            'priority': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Priority'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Due Date', 'type': 'date'}),
        }




        ## esta es una forma echa por chat gpt tiene todo el merito :)
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TaskForm, self).__init__(*args, **kwargs)
        if user:
            # Filtrar las versiones del proyecto basadas en el usuario
            self.fields['project_version'].queryset = ProjectVersion.objects.filter(
                project__projectmember__user=user
            )

            # Obtener miembros del proyecto basados en el usuario
            project_members = ProjectMember.objects.filter(project__projectmember__user=user)

            # Usar un set para obtener IDs únicos de usuarios
            unique_user_ids = set()
            for member in project_members:
                unique_user_ids.add(member.user.id)

            # Crear un queryset a partir de los IDs únicos de usuarios
            self.fields['assigned_to'].queryset = User.objects.filter(id__in=unique_user_ids)

    def clean_assigned_to(self):
        assigned_to = self.cleaned_data['assigned_to']
        if not assigned_to:
            raise forms.ValidationError("Este campo es obligatorio.")
        return assigned_to
    



        ## esta era un forma gracias a chat gpt
    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', None)
    #     super(TaskForm, self).__init__(*args, **kwargs)
    #     if user:
    #         # Filtrar las versiones del proyecto basadas en el usuario
    #         self.fields['project_version'].queryset = ProjectVersion.objects.filter(
    #             project__projectmember__user=user
    #         )

    #         # Obtener miembros del proyecto basados en el usuario
    #         project_members = ProjectMember.objects.filter(project__projectmember__user=user)

    #         # Usar un set para eliminar duplicados
    #         unique_member_ids = set()
    #         unique_members = []
    #         for member in project_members:
    #             if member.user_id not in unique_member_ids:
    #                 unique_member_ids.add(member.user_id)
    #                 unique_members.append(member.id)

    #         # Crear un queryset a partir de los IDs únicos
    #         self.fields['assigned_to'].queryset = ProjectMember.objects.filter(id__in=unique_members)



        ## esta era otra forma gracias a chat gpt
    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', None)
    #     super(TaskForm, self).__init__(*args, **kwargs)
    #     if user:
    #         # Filtrar las versiones del proyecto basadas en el usuario
    #         self.fields['project_version'].queryset = ProjectVersion.objects.filter(
    #             project__projectmember__user=user
    #         )
    #         # Inicialmente, dejar el queryset de assigned_to vacío o con todos los usuarios
    #         self.fields['assigned_to'].queryset = ProjectMember.objects.filter(user=user).select_related('user')
    #     if 'project_version' in self.data:
    #         try:
    #             project_version_id = int(self.data.get('project_version'))
    #             project_version = ProjectVersion.objects.get(id=project_version_id)
    #             self.fields['assigned_to'].queryset = ProjectMember.objects.filter(
    #                 project=project_version.project
    #             ).select_related('user')
    #         except (ValueError, TypeError, ProjectVersion.DoesNotExist):
    #             pass
    #     elif self.instance.pk:
    #         self.fields['assigned_to'].queryset = ProjectMember.objects.filter(
    #             project=self.instance.project_version.project
    #         ).select_related('user')