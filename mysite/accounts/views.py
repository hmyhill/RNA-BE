import json
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm

#When a user accesses the signup endpoint
def signup(request):
    #If they are using a POST request type
    if request.method == 'POST':
        #Generate and then validate their input against a user signup form
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            #Once done, redirect to home page
            return redirect('home')
        #If the user accessing the signup endpoint is ALREADY authenticated, assume they are requesting details of the current user
        if request.user.is_authenticated:
            #Return a response including all relevant information needed by the FE
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
    #If anything goes wrong, just return the signup form itself
    return render(request, 'signup.html', {'form': form})


#If a logged in user attempts to access the change user permissions endpoint
@login_required
def change_user_permissions(request):
    #And uses a POST request
    if request.method == 'POST':
        #And is authenticated
        if request.user.is_authenticated:
            #And is an admin user
            if request.user.is_staff:
                #And the account they are trying to adjust is not their own
                if request.user.username != request.POST['username']:
                    #Change the permissions of the selected user to match whatever is specified in the request
                    updatedUser = User.objects.get(username=request.POST['username'])
                    updatedUser.is_staff = request.POST['is_admin'].lower() == 'true'
                    updatedUser.is_superuser = request.POST['is_admin'].lower() == 'true'
                    updatedUser.save()
                    #And then return their original request back to them
                    return HttpResponse(json.dumps(request.POST))
    #Otherwise throw an error
    raise RuntimeError("An Invalid Request Was Sent")

@login_required
def del_user(request):
    user = request.user
    user.delete()
    return redirect("home")
