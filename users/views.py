from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts' : posts})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {
        'form' : form ,
        'err' : 'registration error'
        })

def login(request):
    pass


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(request, 'create_post.html')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form' : form, 'err' : 'error'})

@login_required
def logout(request):
    logout(request)
    return redirect('post_list.html')