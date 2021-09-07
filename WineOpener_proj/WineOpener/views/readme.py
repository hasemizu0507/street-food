from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
#from django.contrib.auth.decorators import login_required

#import json
#from streetfood.models import Food, Profile, Cart


def readme_view(request):
    return render(request, 'WineOpener/readme.html')
