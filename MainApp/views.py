from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import BlogPostForm
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index1.html')


def blog(request):
    posts = BlogPost.objects.filter().order_by('-dateTime')
    form = BlogPostForm()
    return render(request, 'blog1.html', {'posts':posts, 'form':form})

def blog_single(request, slug):
    post = BlogPost.objects.get(slug=slug)
    comments = Comment.objects.filter(blog=post)
    all_posts = BlogPost.objects.filter().order_by('-dateTime')

    if request.method== "POST":
        user = request.user
        content = request.POST.get('comment')
        comment = Comment(user=user, content=content, blog=post)
        comment.save()
    return render(request, 'blog-single1.html', {'post':post, 'comments':comments, 'all_posts':all_posts})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return redirect('signup')
        
        user = User.objects.create(username=username, email=email, password=password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save() 
        return render(request, 'login.html')


    return render(request, 'signup.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def add_blog(request):
    if request.method == "POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save() 
            alert = True
            return render(request, 'add_blogs.html', {'alert':alert})
    else:
        form  = BlogPostForm()
    return render(request, 'add_blogs.html', {'form':form})


def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        print(searched)
        if searched == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            posts = BlogPost.objects.filter(title__contains=searched) | BlogPost.objects.filter(content__contains=searched)
            return render(request, 'blog1.html', {'posts':posts})