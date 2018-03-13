from django.contrib import admin
from .models import Blog_Type,Blog
# Register your models here.
@admin.register(Blog_Type)
class Blog_TypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','blog_type','author','readed_num','created_time','last_updated_time')
