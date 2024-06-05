from django import forms
from .models import Task

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