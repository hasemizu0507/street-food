from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
from WineOpener.models import Profile, Wine, Cart

@login_required
def mypage_top(request):
    user = request.user
    profile = user.profile
    user_id = user.id # 追加(2021/09/08)
    products = Cart.objects.filter(user_id=user_id) # 追加(2021/09/08)
    return render(request, 'WineOpener/mypage.html', {'profile':profile,'products':products}) #'assessments':myassessments