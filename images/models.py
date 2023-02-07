from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'images_created')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length =200)
    description  = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True,db_index=True)
    image = models.ImageField(upload_to= 'post_image')
    url = models.URLField()
    user_likes = models.ManyToManyField(User,related_name='image_likes',blank= True)

   
    def __str__(self):
        return self.title
    
    def save(self , *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    