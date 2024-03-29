from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Bin, Comment, User
from .forms import BinForm, MyUserCreationForm, UserForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password does not exist')
    context = {'page' : page}
    return render(request, 'app/login_register.html', context)

def logout_page(request):
    logout(request)
    return redirect('home')

def register_page(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'form' : form}
    return render(request, 'app/register_page.html', context)

def home_page(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    bins = Bin.objects.filter(
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    bin_count = bins.count()

    context = {'bins' : bins, 'bin_count' : bin_count}
    return render(request, 'app/home.html', context)

@login_required(login_url = 'login')
def create_bin(request):
    form = BinForm()
    flag = 1

    if request.method == 'POST':
        form = BinForm(request.POST)

        if form.is_valid():
            bin = form.save(commit=False)
            bin.host = request.user
            form.save()
            return redirect('home')

    return render(request, 'app/create-bin.html', context = {'form' : form, 'flag' : flag})

def bin_page(request, pk):
    bin = Bin.objects.get(id = pk)
    comments = bin.comment_set.all().order_by('-created')

    if request.method == 'POST':
        comment = Comment.objects.create(
            user = request.user,
            bin = bin,
            body = request.POST.get('body')
        )
        return redirect('bin', pk = bin.id)

    context = {'bin':bin, 'comments':comments}
    return render(request, 'app/bin-page.html', context)

def about_page(request):
    return render(request, 'app/about_page.html', context = {'workers' : Workers.objects.all()})


@login_required(login_url = 'login')
def update_bin(request, pk):
    bin = Bin.objects.get(id = pk)
    form = BinForm(instance = bin)
    flag = 0

    if request.user != bin.host:
        return HttpResponse('Not allowed 4 u')

    if request.method == 'POST':
        form = BinForm(request.POST, instance = bin)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form' : form, 'flag' : flag, 'bin' : bin}
    return render(request, 'app/create-bin.html', context)

@login_required(login_url = 'login')
def delete_bin(request, pk):
    bin = Bin.objects.get(id = pk)

    if request.user != bin.host:
        return HttpResponse('u are not allowed here')

    if request.method == 'POST':
        bin.delete()
        return redirect('home')

    return render(request, 'app/delete.html', {'obj' : bin})

@login_required(login_url = 'login')
def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.user != comment.user:
        return HttpResponse('u are not allowed here')

    if request.method == 'POST':
        comment.delete()
        return redirect('home')

    return render(request, 'app/delete.html', {'obj': comment})

def user_profile(request, pk):
    user = User.objects.get(id = pk)
    liked_bins = user.bin_like.all()
    bins = user.bin_set.all()
    context = {'user':user, 'bins' : bins, 'liked_bins' : liked_bins}
    return render(request, 'app/user_profile.html', context)

@login_required(login_url = 'login')
def like_bin(request, pk):
    bin = get_object_or_404(Bin, id = request.POST.get('bin_id'))

    if bin.likes.filter(id = request.user.id).exists():
        bin.likes.remove(request.user)

    else:
        bin.likes.add(request.user)

    return redirect('home')

@login_required(login_url = 'login')
def like_from_bin(request, pk):
    bin = get_object_or_404(Bin, id = request.POST.get('bin_id'))

    if bin.likes.filter(id = request.user.id).exists():
        bin.likes.remove(request.user)

    else:
        bin.likes.add(request.user)

    return redirect('bin', pk = bin.id)

@login_required(login_url = 'login')
def update_user(request):
    user = request.user
    form = UserForm(instance = user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect('user_profile', pk = user.id)

    return render(request, 'app/update_user.html', {'form' : form})