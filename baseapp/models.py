from django.db import models
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    no=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100,null=True)
    description=models.TextField()
    date=models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    def formatted_date(self):
        return self.date.strftime('%d/%m/%Y')