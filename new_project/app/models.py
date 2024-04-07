from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    username = models.CharField(max_length = 200, blank = False)
    email = models.EmailField(unique = True, null = True)
    bio = models.TextField(blank = True, default = '')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

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
        if len(self.body) > 50:
            return f'{self.body[0:50]}...'
        else:
            return self.body