from django.shortcuts import render
from django.http import HttpResponse
from .models import UserPass
from .models import Post
from .models import Post1
from .models import Post2
from .models import Post3
from .models import Post4
from django.shortcuts import redirect
from  datetime import datetime
from django.contrib.sessions.models import Session


# Create your views here.
def homepage(request):
    if 'username' in request.session:
        username = request.session['username']
    posts = Post.objects.all()
    posts1 = Post1.objects.all()
    posts2 = Post2.objects.all()
    posts3 = Post3.objects.all()
    posts4 = Post4.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())
'''
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("NO.{}:".format(str(count))+str(post)+"<br>")
        post_lists.append("<small>"+str(post.body.encode('utf=8'))+"</small><br><br>")
    return HttpResponse(post_lists)
'''


def showpost(request, slug):
     try:
         post = Post.objects.get(slug=slug)
         if post != None:
             return render(request,'post.html',locals())
     except:
         return redirect('/')


def showpost1(request, slug):
    try:
        post = Post1.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def showpost2(request, slug):
    try:
        post = Post2.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def showpost3(request, slug):
    try:
        post = Post3.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def showpost4(request, slug):
    try:
        post = Post4.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def login(request):
    if request.method == 'POST' and request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        inDB = UserPass.objects.filter(username=username).first()
        if inDB:
            if password == inDB.password:
                result = 'success'
                request.session['username'] = username
                return render(request,'registerlogin/login.html', {'result': result})
            else:
                result = 'error'
                return render(request,'registerlogin/login.html', {'result': result})
        else:
                result = 'none'
                return render(request,'registerlogin/login.html', {'result': result})
    return render(request,'registerlogin/login.html')


def logout(request):
    if 'username' in request.session:
        Session.objects.all().delete()
        return redirect('/')
    return redirect('/')
