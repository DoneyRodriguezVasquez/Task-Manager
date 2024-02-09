from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    STATUS_CHOICES = [
        ('TO_DO', 'TO DO'),
        ('IN_PROGRESS', 'IN PROGRESS'),
        ('DONE', 'DONE'),
    ]
    PRIORITY_CHOICES = [
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TO_DO')
    comments = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    priority = models.CharField(max_length=40, choices=PRIORITY_CHOICES, default='LOW')
    

    def __str__(self):
        return self.title
    


        