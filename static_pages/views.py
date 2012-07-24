from django.shortcuts import render
from microposts.forms import MicropostForm
from microposts.models import Micropost

def home(request):
    form = MicropostForm()
    user = request.session.get('current_user')
    if user:
        gravatar = user.gravatar()
        micropost_count = Micropost.objects.filter(user=user).count()
        feed_items = user.feed()
    else:
        gravatar = ''
        micropost_count = 0
    return render(request, 'static_pages/home.html', {'form': form,
                                                      'gravatar': gravatar,
                                                      'micropost_count': micropost_count,
                                                      'feed_items': feed_items})

def help(request):
    return render(request, 'static_pages/help.html')

def about(request):
    return render(request, 'static_pages/about.html')

def contact(request):
    return render(request, 'static_pages/contact.html')
