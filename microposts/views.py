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

    if user.is_authenticated():
        up = user.get_profile()
        gravatar = up.gravatar()
        micropost_count = Micropost.objects.filter(user=user).count()
        feed_items = up.feed()
    else:
        up = ''
        gravatar = ''
        micropost_count = 0
        feed_items = ''
    return render(request, 'microposts/home.html', {'form': form,
                                                    'gravatar': gravatar,
                                                    'micropost_count': micropost_count,
                                                    'feed_items': feed_items,
                                                    'user': user,
                                                    'up': up})

    
