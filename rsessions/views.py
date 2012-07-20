from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from forms import SessionForm
from users.models import User

def new(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email__exact=email)
            except User.DoesNotExist:
                user = None
            if user and user.authenticate(password):
                request.session['current_user'] = user
                messages.success(request, 'Login successful.')
                return redirect(user)
            else:
                messages.error(request, 'Invalid email/password combination.')
                return redirect(reverse('signin'))
    else:
        form = SessionForm()

    return render(request, 'rsessions/new.html', {'form': form})

def delete(request):
    if 'current_user' in request.session:
        del request.session['current_user']
    return redirect('home')
