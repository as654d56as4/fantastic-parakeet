from django.shortcuts import render,HttpResponse

def wiki(request,project_id):
    """Wiki首页"""

    return render(request,'wiki.html')


def wiki_add(request,project_id):
    """Wiki添加文章"""

    pass