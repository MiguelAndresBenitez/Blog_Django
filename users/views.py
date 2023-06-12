from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts' : posts})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
        'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                form = UserCreationForm(request.POST)
                form.save()
                login(request, form)
                return redirect('post_list.html')
            except:
                return render(request, 'register.html', {
                'form' : UserCreationForm,
                'err' : 'Username already exists.'
                })
        else:
            return render(request, 'register.html', {
                'form' : UserCreationForm,
                'err' : 'Passwords did not match.'
                })

def user_login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {
        'form' : form
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {"form": AuthenticationForm, "err": "Username or password is incorrect."})
        login(request, user)
        return redirect('post_list')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'my_posts.html', {"posts": posts})

@login_required
def update_post(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id, author=request.user)
        form = PostForm(instance=post)
        return render(request, 'update_post.html', {'post': post, 'form': form})
    else:
        try:
            post = get_object_or_404(Post, pk=post_id, author=request.user)
            form = PostForm(request.POST, instance=post)
            form.save()
            return redirect('my_posts')
        except ValueError:
            return render(request, 'update_post.html', {'post': post, 'form': form, 'error': 'Error updating task.'})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('my_posts')

@login_required
def user_logout(request):
    logout(request)
    return redirect('post_list')