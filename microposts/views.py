from forms import MicropostForm
from models import Micropost
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

def new(request):
    if request.method == 'POST':
        form = MicropostForm(request.POST)
        if form.is_valid():
            micropost = form.save(commit=False)
            micropost.user = request.session['current_user']
            micropost.save()
            messages.success(request, 'Micropost successfully created.')
            return redirect(micropost.user)
    messages.error(request, 'Content field is required.')
    return redirect(reverse('home'))

def delete(request, mp_id):
    if request.method == 'POST':
        micropost = Micropost.objects.get(pk=mp_id)
        user = request.session['current_user']
        if user == micropost.user:
            micropost.delete()
            messages.success(request, 'Micropost deleted.')
            return redirect(user)
