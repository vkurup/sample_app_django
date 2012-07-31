from django.shortcuts import render
from microposts.forms import MicropostForm
from microposts.models import Micropost

def home(request):
    form = MicropostForm()
    user = request.user
    if user:
        up = user.get_profile()
        gravatar = up.gravatar()
        micropost_count = Micropost.objects.filter(user=user).count()
        feed_items = up.feed()
    else:
        gravatar = ''
        micropost_count = 0
        feed_items = ''
    return render(request, 'static_pages/home.html', {'form': form,
                                                      'gravatar': gravatar,
                                                      'micropost_count': micropost_count,
                                                      'feed_items': feed_items,
                                                      'user': user})

def help(request):
    return render(request, 'static_pages/help.html')

def about(request):
    return render(request, 'static_pages/about.html')

def contact(request):
    return render(request, 'static_pages/contact.html')
