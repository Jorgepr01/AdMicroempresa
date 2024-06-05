# from django import forms


# class formProjects(forms.Form):
#     title = forms.CharField(label="Your name", max_length=100)
#     description = forms.CharField(label="Your description", max_length=100)
#     startproject = forms.DateField(label="Your start date", input_formats=['%d/%m/%Y'])
#     endproject = forms.DateField(label="Your end date", input_formats=['%d/%m/%Y'])
from django import forms
from django.forms import ModelForm
from django.forms import modelformset_factory
from .models import Project,ProjectVersion,ProjectMember

class formProjects(ModelForm):
    
    class Meta:
        model = Project
        # fields = ['name','team','description','start_date','end_date']
        fields = ['name','description','start_date','end_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Name'}),
            # 'team': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Project Description', 'rows': 4}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

ProyectoFormSet = modelformset_factory(Project, form=formProjects, extra=0)

class formProjectVersions(ModelForm):
    class Meta:
        model = ProjectVersion
        fields = ['project','version_number','release_date','notes']
        widgets = {
            'project': forms.Select(attrs={'class': 'form-select'}),
            'version_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Version Number'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notes', 'rows': 4}),
        }

class FormProjectMember(forms.ModelForm):
    class Meta:
        model = ProjectMember
        fields = ['user','project','role']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),
            'team': forms.Select(attrs={'class': 'form-select'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Role'}),
        }
