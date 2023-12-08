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
                "is_authenticated": request.user.is_authenticated()
            }), content_type='application/json')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def del_user(request):
    user = request.user
    user.delete()
    return redirect("home")
