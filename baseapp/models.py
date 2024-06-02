from django.db import models

# Create your models here.


class Task(models.Model):
    no=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100,null=True)
    description=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.title