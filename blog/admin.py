from django.contrib import admin
from .models import Blog_Type,Blog
# Register your models here.
@admin.register(Blog_Type)
class Blog_TypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','blog_type','author','created_time','last_updated_time')
'''
@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num','blog')
'''