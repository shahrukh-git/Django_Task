from django.db import models

class User(models.Model):
    # first_name, last_name, email, password, username
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
    
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.CharField(max_length=20)
    text = models.TextField(max_length=400)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

