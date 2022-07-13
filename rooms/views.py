from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models

def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5) # 마지막페이지에 15개까지 넣음 (16개 넘어가면 다음페이지 생성)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")