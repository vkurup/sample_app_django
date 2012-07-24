from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import User
from forms import UserForm
from microposts.models import Micropost

def new(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, 'Profile successfully created.')
            request.session['current_user'] = new_user
            return redirect(new_user)
    else:
        form = UserForm()

    return render(request, 'users/new.html', {'form': form})

def show(request, user_id):
    user = User.objects.get(id=user_id)
    microposts_list = Micropost.objects.filter(user=user_id)
    paginator = Paginator(microposts_list, 50)

    page = request.GET.get('page')
    try:
        microposts = paginator.page(page)
    except PageNotAnInteger:
        microposts = paginator.page(1)
    except EmptyPage:
        microposts = paginator.page(paginator.num_pages)

    return render(request, 'users/show.html', {'user': user,
                                               'microposts': microposts})

def index(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        # create
        return render(request, 'users/show.html', {})

def edit(request, user_id):
    if 'current_user' not in request.session:
        messages.warning(request, 'Please sign in.')
        return redirect(reverse('signin'))
    if request.session['current_user'].id != int(user_id):
        return redirect(reverse('home'))
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            edited_user = form.save()
            messages.success(request, 'Profile successfully edited.')
            request.session['current_user'] = edited_user
            return redirect(edited_user)
    else:
        form = UserForm(instance=user)

    return render(request, 'users/edit.html', {'form': form,
                                               'user': user})
