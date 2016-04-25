import json

from django.core import serializers
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import Champion, Role, WinRate, Item, ItemBuild
from serializers import ChampionSerializer, RoleSerializer, ItemSerializer, BuildSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
import os

def index(request):
    content = ''

    # super hacky and I'm sorry. Fixes problems with Django + Angular templates
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/champion_picker/index.html')) as f:
        content = f.read()
    return HttpResponse(content)

def builder(request):
    content = ''

    # super hacky and I'm sorry. Fixes problems with Django + Angular templates
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/champion_picker/champion_picker.html')) as f:
        content = f.read()
    return HttpResponse(content)

@csrf_exempt
def get_matchup(request):
    js_data = request.body

    request_data = json.loads(js_data)

    team_one = request_data["team1"]
    team_two = request_data["team2"]

    team_matchups = []

    banned_roles = []
    bans = request_data["bans"]
    turn = request_data["turn"]

    for b in bans:
        current_ban = Role.objects.get(id=b)
        banned_roles.append(current_ban)

    for t in team_one:
        banned_roles.append(Role.objects.get(id=int(t)))
    for t in team_two:
        banned_roles.append(Role.objects.get(id=int(t)))

    print("BANS: " + str(banned_roles))

    if turn == 1:
        for role_o in team_two:
            current_role = Role.objects.get(id=role_o)
            best_matchups = WinRate.objects.filter(Q(role2=current_role) & ~Q(role1__in=banned_roles)).order_by('-win_rate')[0:5]
            if len(best_matchups) == 0:
                best_matchups = WinRate.objects.filter(Q(role2=current_role) & ~Q(role1__in=banned_roles)).order_by('-win_rate')[0:5]
            team_matchups.append(best_matchups)
            print(str(current_role) + ": " + str(best_matchups))
    elif turn == 2:
        for role_o in team_one:
            current_role = Role.objects.get(id=role_o)
            best_matchups = WinRate.objects.filter(Q(role2=current_role) & ~Q(role1__in=banned_roles)).order_by('-win_rate')[0:5]
            if len(best_matchups) == 0:
                best_matchups = WinRate.objects.filter(Q(role2=current_role) & ~Q(role1__in=banned_roles)).order_by('-win_rate')[0:5]
            team_matchups.append(best_matchups)
            print(str(current_role) + ": " + str(best_matchups))

    final_data = {}

    for m in team_matchups:
        entry_line = []
        srole = ""
        for c in m:
            entry_line.append({"role1": c.role1.champion.name, "role2": c.role2.champion.name, "portrait": c.role1.champion.portrait_image.name, "win_rate": float(c.win_rate)})
            srole = c.role2.champion.name
        final_data[str(srole)] = entry_line

    return HttpResponse(json.dumps(final_data))

def builder(request):
    content = ''

    # super hacky and I'm sorry. Fixes problems with Django + Angular templates
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/champion_picker/champion_picker.html')) as f:
        content = f.read()
    return HttpResponse(content);

class ChampionViewSet(viewsets.ViewSet):
    """
    ViewSet for listing and retrieving champions.
    """
    queryset = Champion.objects.all()

    def list(self, request):
        queryset = self.queryset.all()
        serializer = ChampionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset.all()
        champ = get_object_or_404(queryset, pk=pk)
        serializer = ChampionSerializer(champ)
        return Response(serializer.data)

    @detail_route()
    def roles(self, request, pk=None):
        queryset = self.queryset.all()
        champ = get_object_or_404(queryset, pk=pk)
        roles = champ.role_set.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)


class RoleViewSet(viewsets.ViewSet):
    """
    ViewSet for roles.
    """
    queryset = Role.objects.all()

    def list(self, request):
        queryset = self.queryset.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset.all()
        role = get_object_or_404(queryset, pk=pk)
        serializer = RoleSerializer(role)
        return Response(serializer.data)


class ItemViewSet(viewsets.ViewSet):
    """
    ViewSet for items.
    """
    queryset = Item.objects.all()

    def list(self, request):
        queryset = self.queryset.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)


class BuildViewSet(viewsets.ViewSet):
    """
    ViewSet for champions' item builds.
    """
    queryset = ItemBuild.objects.all()

    def list(self, request):
        queryset = self.queryset.all()
        serializer = BuildSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset.all()
        build = get_object_or_404(queryset, pk=pk)
        serializer = BuildSerializer(build)
        return Response(serializer.data)

