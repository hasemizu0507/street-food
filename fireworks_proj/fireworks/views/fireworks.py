from django.shortcuts import render, redirect, get_object_or_404 # 追加(2021.08.28.10:43)
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages


from django.core.paginator import Paginator
from fireworks.models import Fireworks

import random

from django.contrib.auth.decorators import login_required # 追加(2021.08.28)

def list_view(request):
    fireworks_list = Fireworks.objects.all().order_by('-id')
    paginator = Paginator(fireworks_list, 20) # ページ当たり20個表示

    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    fireworks_list = paginator.get_page(page) # 変更(2021.08.28.11:42)
    return render(request, 'fireworks/fireworks_list.html', {'fireworks_list': fireworks_list, 'page': page, 'last_page': paginator.num_pages})

def detail_view(request, fireworks_id):
    fireworks = get_object_or_404(Fireworks, id=fireworks_id)

    try:
        page = int(request.GET.get('from_page'))
    except:
        page = 1
    return render(request, 'fireworks/fireworks_detail.html', {'fireworks': fireworks, 'page': page })