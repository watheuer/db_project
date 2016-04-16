from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from models import Champion, Role, WinRate, Item, ItemBuild
from serializers import ChampionSerializer, RoleSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route


def index(request):
    context = {}
    return render(request, 'champion_picker/index.html', context)

class ChampionViewSet(viewsets.ViewSet):
    """
    ViewSet for listing and retrieving champions.
    """
    queryset = Champion.objects.all()

    def list(self, request):
        serializer = ChampionSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        champ = get_object_or_404(self.queryset, pk=pk)
        serializer = ChampionSerializer(champ)
        return Response(serializer.data)

    @detail_route()
    def roles(self, request, pk=None):
        champ = get_object_or_404(self.queryset, pk=pk)
        roles = champ.role_set.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)


class RoleViewSet(viewsets.ViewSet):
    """
    ViewSet for roles.
    """
    queryset = Role.objects.all()

    def list(self, request):
        serializer = RoleSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        role = get_object_or_404(self.queryset, pk=pk)
        serializer = RoleSerializer(role)
        return Response(serializer.data)

# def all(request):
#     champions = Champion.objects.all()
#     return JsonResponse({'champions': ['...']})
# 
# def detail(request, champion_id):
#     return JsonResponse({'id': champion_id})
# 
# def role(request, role_id):
#     return JsonResponse({'role_id': role_id})
# 
# def matchups(request, role_id):
#     return JsonResponse({'role_id': role_id})
# 
# def builds(request, role_id):
#     return JsonResponse({'role_id': role_id})
# 
# def items(request):
#     items = Item.objects.all()
#     return JsonResponse({'items': '...'})
