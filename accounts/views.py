from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from forms import MyUserCreationForm, UserEditForm
from microposts.models import Micropost

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            messages.success(request, 'Profile successfully created.')
            return redirect(reverse('home'))
    else:
        form = MyUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect(reverse('home'))

def show(request, username):
    user = User.objects.get(username=username)
    microposts_list = Micropost.objects.filter(user=user.id)
    paginator = Paginator(microposts_list, 50)
    button = None
    up = user.get_profile()

    if request.user.is_authenticated():
        if user != request.user:
            request_profile = request.user.get_profile()
            if request_profile.following_p(user):
                button = 'unfollow'
            else:
                button = 'follow'

    page = request.GET.get('page')
    try:
        microposts = paginator.page(page)
    except PageNotAnInteger:
        microposts = paginator.page(1)
    except EmptyPage:
        microposts = paginator.page(paginator.num_pages)

    return render(request, 'accounts/show.html', {'user': user,
                                                  'up': up,
                                                  'microposts': microposts,
                                                  'button': button})

@login_required
def edit(request, user_id):
    if request.user.id != int(user_id):
        return redirect(reverse('home'))
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            edited_user = form.save()
            messages.success(request, 'Profile successfully edited.')
            return redirect(edited_user)
    else:
        form = UserEditForm(instance=user)

    return render(request, 'accounts/edit.html', {'form': form,
                                                  'user': user})


@login_required
def follow(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        up = request.user.get_profile()
        up.follow(user)
        return redirect(user)

@login_required
def unfollow(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        up = request.user.get_profile()
        up.unfollow(user)
        return redirect(user)


def following(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    up = user.get_profile()
    title = "Following"
    users_list = up.followed_users.all()
    paginator = Paginator(users_list, 50)

    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'accounts/show_follow.html', {'user': user,
                                                         'title': title,
                                                         'users': users})

def followers(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    up = user.get_profile()
    title = "Followers"
    users_list = up.followers.all()
    paginator = Paginator(users_list, 50)

    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'accounts/show_follow.html', {'user': user,
                                                         'title': title,
                                                         'users': users})
