import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRMPROJECT.settings')
from django.utils import timezone
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete= models.CASCADE , null=True)
    def __str__(self):
        return self.user.email


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent,null=True,blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category",related_name='leads' ,null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name

class Category(models.Model):
    name = models.CharField(max_length=30)
    organisation = models.ForeignKey(UserProfile, on_delete= models.CASCADE , null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



def post_user_created_signal(sender,instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)