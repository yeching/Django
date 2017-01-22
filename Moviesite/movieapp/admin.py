from django.contrib import admin

# Register your models here.
from .models import Movie,User
admin.site.register(Movie)
admin.site.register(User)

