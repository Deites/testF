from django.contrib import admin
from .models import Post, Comment
from django.urls import path
from django.shortcuts import HttpResponseRedirect
from .models import Comment
from django.shortcuts import get_list_or_404

admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    change_form_template = 'admin/change_form_delete_comment.html'
    
