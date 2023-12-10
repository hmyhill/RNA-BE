import json
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
        if request.user.is_authenticated:
            return HttpResponse(json.dumps({
                "is_authenticated": request.user.is_authenticated,
                "is_admin": request.user.is_staff,
                "username": request.user.username,
                "email": request.user.email,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name
            }), content_type='application/json')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def change_user_permissions(request):
    print("TEST")
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user.is_staff:
                print("CHECKING USER PERMS")
                if request.user.username != request.POST['username']:
                    print("UPDATING")
                    updatedUser = User.objects.get(username=request.POST['username'])
                    updatedUser.is_staff = request.POST['is_admin'].lower() == 'true'
                    updatedUser.is_superuser = request.POST['is_admin'].lower() == 'true'
                    updatedUser.save()
                    return HttpResponse(json.dumps(request.POST))
    raise RuntimeError("An Invalid Request Was Sent")

@login_required
def del_user(request):
    user = request.user
    user.delete()
    return redirect("home")
