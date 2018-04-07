from django.urls import path
from . import views

urlpatterns = [
    #文章ID
    path('update_comment',views.update_comment,name='update_comment')
]
