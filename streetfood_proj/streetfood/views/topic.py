from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages


from django.core.paginator import Paginator
from streetfood.models import Food

import random

def live_view(request):
    foods = Food.objects.all().order_by('-id')
    return render(request, 'streetfood/topic_live.html', {'foods': foods})

