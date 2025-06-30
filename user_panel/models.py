from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length = 200)
    status_choices = [('open', 'OPEN'),( 'in-progress', 'In Progress'), ('finished', 'FINISHED'),]
    description = models.TextField()
    creation_date = models.DateTimeField("Date Created", default = datetime.now)
    status = models.CharField(max_length = 20, choices = status_choices, default = 'open',)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    
def __str__(self):
    return self.title