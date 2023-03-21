
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login
from renting_wbscp.forms import UserForm
from django.views import generic
# Create your views here.


def contact_view(request):
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')

def explore_view(request):
    return render(request, 'explore.html')

def user_data_view(request):
    return render(request, 'user_data.html')

# def login(request):
#     return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            user = form_user.save()
            user.refresh_from_db()
            user.save()
            login(request, user)
            # subject = ''
            # message = ''
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [user.email, ]
            # send_mail(subject, message, email_from, recipient_list)
            return redirect('index')
    else:
        form_user = UserForm()
    return render(request, 'signup.html', {"form": form_user})
