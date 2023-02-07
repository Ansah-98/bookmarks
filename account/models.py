from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete= models.CASCADE , related_name='profile')
    date_of_birth = models.DateField(blank=True,null=True )
    photo = models.ImageField(upload_to= 'images/')

    def __str__(self):
        return f'Profile for user {self.user.username}'