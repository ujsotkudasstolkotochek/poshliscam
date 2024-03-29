from django.contrib import admin
from app.models import Bin, Comment, User

admin.site.register(Bin)
admin.site.register(Comment)
admin.site.register(User)