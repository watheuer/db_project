from django.shortcuts import render
from django.http import JsonResponse
from models import Champion, Role, WinRate, Item, ItemBuild

def index(request):
    champions = Champion.objects.all()
    return JsonResponse({'hello':'world'})

def detail(request, champion_id):
    return JsonResponse({'id': champion_id})
