from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name
    

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='created')
    users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.project_name