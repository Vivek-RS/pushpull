from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Message, Comment

@login_required
def feed(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            message = Message(user=request.user, content=content)
            message.save()
    messages = Message.objects.all().order_by('-created_at')
    context = {'messages': messages}
    return render(request, 'feed.html', context)

@login_required
def delete_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if message.user == request.user:
        message.delete()
    return redirect('feed')

@login_required
def like_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.user in message.likes.all():
        message.likes.remove(request.user)
    else:
        message.likes.add(request.user)
    return redirect('feed')

@login_required
def add_comment(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('comment')
        if content:
            comment = Comment(user=request.user, message=message, content=content)
            comment.save()  # No need to specify the database for saving
    return redirect('feed')

@login_required
def like_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    return redirect('feed')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username and email and password:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('feed')
            except Exception as e:
                print(e)  # Handle registration error
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('register')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            pass
    return render(request, 'login.html')
