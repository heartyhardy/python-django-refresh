from django.contrib import admin

# Register your models here.
from .models import Author, Todo

admin.site.register(Author)
admin.site.register(Todo)