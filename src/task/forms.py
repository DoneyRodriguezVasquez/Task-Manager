from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project', 'date', 'assigned_to', 'state', 'comments']
        widgets = {
            'title' : forms.TextInput(
                attrs={
                'class': 'form-control',
                'id': 'floatingInput',
            }),
            'description' : forms.Textarea(
                attrs={
                'class': 'form-control',
                'id': 'floatingTextarea',
                'style': 'height: 150px'
                }
            ),
            'project' : forms.Select(
                attrs={
                'class': 'form-select',
                'id': 'floatingSelect3',
                'aria-label': '',
                }
            ),
            'date': forms.TextInput  (
                attrs={
                'class': 'form-control',
                'id': 'floatingInput2',
                'type': 'date'
                }
            ),
            'assigned_to' : forms.Select(
                attrs={
                'class': 'form-select',
                'id': 'floatingSelect',
                'aria-label': '',
                }
            ),
            'state': forms.Select(
                attrs={
                    'class': 'form-select',
                    'id': 'floatingSelect2',
                }
            ),
            'comments' : forms.Textarea(
                attrs={
                'class': 'form-control',
                'id': 'floatingTextarea2',
                'style': 'height: 200px'
                }
            ),
        }


        
