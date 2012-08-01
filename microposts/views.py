from forms import MicropostForm
from models import Micropost
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

@login_required
def new(request):
    if request.method == 'POST':
        form = MicropostForm(request.POST)
        if form.is_valid():
            micropost = form.save(commit=False)
            micropost.user = request.user
            micropost.save()
            messages.success(request, 'Micropost successfully created.')
            return redirect(reverse('home'))
    messages.error(request, 'Content field is required.')
    return redirect(reverse('home'))

@login_required
def delete(request, mp_id):
    if request.method == 'POST':
        micropost = Micropost.objects.get(pk=mp_id)
        if request.user == micropost.user:
            micropost.delete()
            messages.success(request, 'Micropost deleted.')
            return redirect(reverse('home'))

def home(request):
    form = MicropostForm()
    user = request.user

    return render(request, 'microposts/home.html', {'form': form,
                                                    'user': user})
