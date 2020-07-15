from django.shortcuts import render
from basicapp.forms import UserForm, UserProfileInoForm

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.htm')

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        userprofile_form = UserProfileInoForm(data=request.POST)

        if user_form.is_valid() and userprofile_form.is_valid(): 
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = userprofile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

        else:
            print("Invalid user")
            return (user_form.errors, UserProfileInoForm.errors)
    else:
        user_form = UserForm()
        userprofile_form = UserProfileInoForm()

    return render(request, 'basicapp/register.htm',{
        'user_form':user_form, 'user_profile':userprofile_form
    })


#LOGIN
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print("Unknow user is trying to login {}".format(username))
            return HttpResponse("USER IS INVALID")
    else: 
        return render(request, 'basicapp/login.htm',{

        })

#Logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))