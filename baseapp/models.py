from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    no=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100,null=True)
    description=models.TextField()
    date=models.DateField(default=timezone.now)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def formatted_date(self):
        return self.date.strftime('%d/%m/%Y')
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
