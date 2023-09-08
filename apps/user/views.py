from django.shortcuts import render
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
