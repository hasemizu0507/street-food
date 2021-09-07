from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json


@login_required
def mypage_top(request):
    user = request.user
    profile = user.profile
    return render(request, 'WineOpener/mypage.html', {'profile':profile}) #'assessments':myassessments