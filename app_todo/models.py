from django.db import models

class Task(models.Model):
    
    title = models.CharField(max_length=100)
    body = models.TextField(blank= True)
    completed = models.DateField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title