from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=255)
    is_online = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    owner = models.IntegerField()
    other_user = models.IntegerField()
    chat_no = models.CharField(max_length=255)


class Message(models.Model):
    message = models.CharField(max_length=1000)
    sender = models.IntegerField()
    reciever = models.IntegerField()
    read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
