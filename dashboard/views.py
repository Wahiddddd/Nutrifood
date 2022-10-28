from collections import Counter
from django.shortcuts import render

from dashboard.models import UserTop5

def index(request):
    user_list = UserTop5.objects.filter().order_by('-points')[:5]
    context = {
        'user_list': user_list,
    }
    return render(request, 'dashboard/index.html', context)