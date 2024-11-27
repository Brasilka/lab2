from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user_profile(request, username):
    return render(request, 'user_profile.html', {'username': username})

def post_detail(request, post_id):
    return render(request, 'post_detail.html', {'post_id': post_id})