from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return JsonResponse({'hello':'world'})

def detail(request, champion_id):
    return JsonResponse({'id': champion_id})
