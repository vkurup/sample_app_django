from django.shortcuts import render_to_response

def home(request):
    return render_to_response('static_pages/home.html')

def help(request):
    return render_to_response('static_pages/help.html')

def about(request):
    return render_to_response('static_pages/about.html')
