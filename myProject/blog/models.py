from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')



class Post(models.Model):
    title = models.CharField(max_length=255,default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title_tag = models.CharField(max_length=255, default=None)
    body = models.TextField(default = None)
    post_date = models.DateTimeField(auto_now_add=True)
    category =models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='images/')
    
    
    
    def __str__(self):
        return self.title + " | " + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')