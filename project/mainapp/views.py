from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Room, Post


def home(request):
    return render(request, 'mainapp/index.html')


def show_room(request, room_name):
    users = Room.objects.get(name=room_name)
    print(users.users)
    name = Room.objects.get(name=room_name)
    posts = Post.objects.filter(room__name=room_name)
    return render(request, 'mainapp/show_room.html', {'name':name, 'posts':posts})


def create_post(request, room_name):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.room = Room.objects.get(name=room_name)
            form.save()

            return redirect(f'/room/{room_name}')
    else:
        form = PostForm()

    return render(request, 'mainapp/create_post.html', {'form':form})
