from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
#from django.contrib.auth.decorators import login_required

#import json
#from streetfood.models import Food, Profile, Cart # 変更予定(2021/09/07)


def list_view(request):
    return render(request, 'WineOpener/live_list.html')

def detail_view(request):
    return render(request, 'WineOpener/live_detail.html')