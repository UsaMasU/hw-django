
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from .forms import SignUpForm
from .forms import LoginForm


from django.contrib.auth.models import User, Permission


def user_login(request):
    if request.method == 'POST':

        users_list = User.objects.filter(email=request.POST['email'])
        for user in users_list:
            print(user.email)

        form = LoginForm(request.POST)

        print('errors:', form.errors)

        for field in form:
            print(field.name, field.value())

        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return render(request, 'app_users/login.html',  {'message': 'user_disabled'})
            else:
                return render(request, 'app_users/login.html',  {'message': 'error_login'})
    else:
        form = LoginForm()
    return render(request, 'app_users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')


# @login_required(login_url="/")
def user_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.first_name = form['first_name'].value()
            user.last_name = form['last_name'].value()
            user.email = form.cleaned_data.get('email')
            user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        login(request, authenticate(username=username, password=password))
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
