from django.shortcuts import render_to_response

def new(request):
    return render_to_response('users/new.html')
