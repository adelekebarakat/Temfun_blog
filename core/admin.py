from django.contrib import admin
from .models import Post, core_category, Profile, Comment

# Register your models here.



admin.site.register(Post,)
admin.site.register(core_category)
admin.site.register(Profile)
admin.site.register(Comment)
