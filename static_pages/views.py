from django.shortcuts import render

def home(request):
    return render(request, 'static_pages/home.html', locals())

def help(request):
    return render(request, 'static_pages/help.html', locals())

def about(request):
    return render(request, 'static_pages/about.html', locals())

def contact(request):
    return render(request, 'static_pages/contact.html', locals())
