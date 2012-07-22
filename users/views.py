import hashlib
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from models import User
from forms import UserForm

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
    gravatar_id = hashlib.md5(user.email.lower()).hexdigest()
    gravatar_url = "https://secure.gravatar.com/avatar/%s" % (gravatar_id)
    return render(request, 'users/show.html', {'user': user,
                                               'gravatar_url': gravatar_url})

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
    gravatar_id = hashlib.md5(user.email.lower()).hexdigest()
    gravatar_url = "https://secure.gravatar.com/avatar/%s" % (gravatar_id)
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
                                               'user': user,
                                               'gravatar_url': gravatar_url})
