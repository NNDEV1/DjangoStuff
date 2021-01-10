from django.shortcuts import render
from basicapp.forms import UserForm, UserProfileInfoForm, PostForm
from django.contrib.auth.models import User
from basicapp.models import UserProfileInfo


from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(password=password, username=username)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active, Have You Registered?')

        else:
            print("Someone Tried To Login And Failed")
            print("Username: {}, Password: {}".format(username, password))
            return HttpResponse('login failed')

    else:
        return render(request, 'basicapp/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def user_post(request):
    form = PostForm(request.POST)
    form_class = form(request.POST or None)
    if form.is_valid():
        text = form.cleaned_data['post']
        form = PostForm()
        return HttpResponseRedirect(reverse('index'))
    else:
        HttpResponse("Not Valid try dat boi agian")

    render(request, 'basicapp/userpost.html', 
                    {'form':form,
                     'text':text})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basicapp/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})



