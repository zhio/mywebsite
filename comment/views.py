from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.http import JsonResponse
from .models import Comment
from .forms import CommentForm

# Create your views here.

def update_comment(request):
    '''referer = request.META.get('HTTP_REFERER',reverse('home'))
    user = request.user
    if not user.is_authenticated:
        return render(request,'error.html',{'message':'用户未登录','redirect_to':referer})
    text = request.POST.get('text', '').strip()
    if text == '':
        return render(request,'error.html',{'message':'评论内容为空','redirect_to':referer})
    try:
        content_type=request.POST.get('content_type', '')
        object_id = int(request.POST.get('object_id', ''))
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except Exception as e:
        return render(request,'error.html',{'message':'评论对象为空','redirect_to':referer})

    comment = Comment()
    comment.user = user
    comment.text = text
    comment.content_object = model_obj
    comment.save()
    return redirect(referer)'''

    referer = request.META.get('HTTP_REFERER',reverse('home'))
    comment_form=CommentForm(request.POST,user=request.user)
    data = {}

    if comment_form.is_valid():
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']
        comment.save()

        data['status'] = 'SUCCESS'
        data['username'] = comment.user.username
        data['comment_time'] = comment.comment_time.strftime('%Y-%m-%d %H:%M:%S')
        data['text'] = comment.text
    else:
        data['status'] = 'ERROR'
        data['message'] = list(comment_form.errors.values())[0][0]
    return JsonResponse(data)