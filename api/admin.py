from django.contrib import admin
from .models import Comment, Author, Blog
# Register your models here.

admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Blog)
