from typing import Optional
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from . models import User

# Create your views here.


def users_list(request):
    users = User.objects.all()
    user_cnt = users.count()

    context = {
        'users': users,
        "user_count": user_cnt
    }

    return render(request, 'user/user_list.html', context)


def login_view(request):
    error_message = None
    # Unbound form
    form = AuthenticationForm()
    # Bound form
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        # Validate
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticate the user
            user: Optional[User] = authenticate(
                username=username,
                password=password,
            )

            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                error_message = 'Sorry, something went wrong'

    context = {'form': form, 'error_message': error_message}
    return render(request, "user/login.html", context)


def profile(request):
    return render(
        request,
        "user/profile.html")
