from django.shortcuts import render
from django.http import JsonResponse
from models import Champion, Role, WinRate, Item, ItemBuild

def index(request):
    context = {}
    return render(request, 'champion_picker/index.html', context)

def all(request):
    champions = Champion.objects.all()
    return JsonResponse({'champions': ['...']})

def detail(request, champion_id):
    return JsonResponse({'id': champion_id})

def role(request, role_id):
    return JsonResponse({'role_id': role_id})

def matchups(request, role_id):
    return JsonResponse({'role_id': role_id})

def builds(request, role_id):
    return JsonResponse({'role_id': role_id})

def items(request):
    items = Item.objects.all()
    return JsonResponse({'items': '...'})
