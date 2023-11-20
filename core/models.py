from django.db import models
from django.contrib.auth import get_user_model

from django.urls import reverse
from ckeditor.fields import RichTextField





# Create your models here.
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=225)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    

    def __str__(self):
        return self.name
    
  

    def get_absolute_url(self):
        return reverse('home')
    


class Post(models.Model):
    title = models.CharField(max_length=225)
    title_tag = models.CharField(max_length=225)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length = 225, default = 'coding')
    intro = models.TextField()
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    class Meta:
        ordering = ( '-created_at', )

    def __str__(self):
        return self.title + ' | ' + str(self.owner)
    
    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile', null=True, blank=True)
    website_url = models.CharField(max_length=225, null=True, blank=True) 
    facebook_url = models.CharField(max_length=225, null=True, blank=True) 
    instagram_url = models.CharField(max_length=225, null=True, blank=True) 
    pinterest_url = models.CharField(max_length=225, null=True, blank=True) 
    twitter_url = models.CharField(max_length=225, null=True, blank=True) 



    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')
    


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete= models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return ' %s - %s ' % (self.post.title, self.name)
    

    def get_absolute_url(self):
        return reverse('home')
    

