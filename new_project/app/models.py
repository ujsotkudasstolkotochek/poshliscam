from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(unique = True, null = True)
    bio = models.TextField(null = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Workers(models.Model):
    name = models.CharField(max_length = 999, blank = False)
    second_name = models.CharField(max_length = 999, blank = True)
    third_name = models.CharField(max_length = 999, blank = True)
    selery = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.name} {self.second_name}'

class Bin(models.Model):
    host = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length = 999, blank = False)
    description = models.TextField(null = False)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    likes = models.ManyToManyField(User, related_name = 'bin_like' )

    class Meta:
        ordering = ['-updated', '-created']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.name



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    bin = models.ForeignKey(Bin, on_delete = models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body[0 : 50]