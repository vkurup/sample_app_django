from django.shortcuts import render

def help(request):
    return render(request, 'static_pages/help.html')

def about(request):
    return render(request, 'static_pages/about.html')

def contact(request):
    return render(request, 'static_pages/contact.html')
