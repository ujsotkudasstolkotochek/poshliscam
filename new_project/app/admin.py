from django.contrib import admin
from app.models import Workers, Bin, Comment, User

admin.site.register(Workers)
admin.site.register(Bin)
admin.site.register(Comment)
admin.site.register(User)