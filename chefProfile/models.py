import uuid

from django.db import models

def __user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)

class Profile(models.Model):
    userID = models.UUIDField(default = uuid.uuid4, editable = False)  # TODO Replace with Django User model
    name = models.CharField(max_length = 50)
    birthdate = models.DateField("Birth date")
    profilePicture = models.ImageField(upload_to = user_directory_path)
    # TODO additional fields, alternatively make a few different models for
    # profiles to reduce size

class Recipe(models.Model):
    chefID = models.UUIDField(default = False, editable = True)
    name = models.CharField(max_length = 200)
    publishDate = models.DateField(auto_now = True)
    estimated_time = models.TimeField()
    directions = models.TextField()
    # TODO additional fields
