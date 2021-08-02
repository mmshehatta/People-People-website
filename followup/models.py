from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    questions = models.CharField(max_length=500 , null=False , blank=False , unique=False)
    answer = models.CharField(max_length=500 , null=False , blank=False , unique=False)
    status = models.IntegerField()

class ContactUs(models.Model):
    name = models.CharField(max_length=100 , null=False , blank=False , unique=False)
    email = models.EmailField(max_length = 254)
    message = models.CharField(max_length=1000 , null=False , blank=False , unique=False)
    seen = models.IntegerField()

class Review(models.Model):
    content = models.CharField(max_length=500 , null=False , blank=False , unique=False)
    publish = models.IntegerField(default=0)

    # Relation with users by user_id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
