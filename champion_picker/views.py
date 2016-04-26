import json

from django.core import serializers
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from champion_picker.models import Champion, Role, WinRate, Item, ItemBuild
from champion_picker.serializers import ChampionSerializer, RoleSerializer, ItemSerializer, BuildSerializer
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

    team_one_str = request_data["team1"]
    team_two_str = request_data["team2"]



    team_matchups = []

    banned_roles = []
    bans = request_data["bans"]
    turn = request_data["turn"]

    for b in bans:
        rel_champ = Champion.objects.get(name=b)
        current_ban = Role.objects.filter(champion=rel_champ)
        # print("INITIAL BAN - CHAMPION " + str(rel_champ.name) + " SQL: " + str(current_ban.query))
        for c in current_ban:
            banned_roles.append(c)


    team_one = []
    team_two = []
    if turn == 1:
        if len(team_two_str) == 0:
            if len(bans) == 0:
                all_roles = Role.objects.all()
                serializer = RoleSerializer(all_roles, many=True)
                return HttpResponse(json.dumps(serializer.data))
            else:
                bnames = []
                for b in banned_roles:
                    bnames.append(b.champion.name)
                all_roles = Role.objects.filter(~Q(champion__name__in=bnames))
                serializer = RoleSerializer(all_roles, many=True)
                return HttpResponse(json.dumps(serializer.data))
        for champ in team_one_str:
            tc = Champion.objects.get(name=champ)
            roles_for_champ = Role.objects.filter(champion=tc)
            print("TEAM ONE BAN SQL: " + str(roles_for_champ.query))
            for r in roles_for_champ:
                team_one.append(str(r.id))
        for champ in team_two_str:
            tc = Champion.objects.get(name=champ)
            roles_for_champ = Role.objects.filter(champion=tc)
            print("TEAM TWO BAN SQL: " + str(roles_for_champ.query))
            for r in roles_for_champ:
                team_two.append(str(r.id))
        for t in team_one:
            banned_roles.append(Role.objects.get(id=int(t)))
        for t in team_two:
            banned_roles.append(Role.objects.get(id=int(t)))
        for role_o in team_two:
            current_role = Role.objects.get(id=role_o)
            best_matchups = WinRate.objects.filter(Q(role2=current_role) & ~Q(role1__in=banned_roles)).order_by('-win_rate')[0:5]
            if len(best_matchups) == 0:
                best_matchups = WinRate.objects.filter(Q(role1=current_role) & ~Q(role2__in=banned_roles)).order_by('-win_rate')[0:5]
            print("TEAM ONE MATCHUP SQL: " + str(best_matchups.query))
            team_matchups.append(best_matchups)
            print(str(current_role) + ": " + str(best_matchups))
    elif turn == 2:
        if len(team_one_str) == 0:
            if len(bans) == 0:
                all_roles = Role.objects.all()
                serializer = RoleSerializer(all_roles, many=True)
                return HttpResponse(json.dumps(serializer.data))
            else:
                bnames = []
                for b in banned_roles:
                    bnames.append(b.champion.name)
                all_roles = Role.objects.filter(~Q(champion__name__in=bnames))
                serializer = RoleSerializer(all_roles, many=True)
                return HttpResponse(json.dumps(serializer.data))
        for champ in team_one_str:
            tc = Champion.objects.get(name=champ)
            roles_for_champ = Role.objects.filter(champion=tc)
            for r in roles_for_champ:
                team_one.append(str(r.id))
        for champ in team_two_str:
            tc = Champion.objects.get(name=champ)
            roles_for_champ = Role.objects.filter(champion=tc)
            for r in roles_for_champ:
                team_two.append(str(r.id))
        for t in team_one:
            banned_roles.append(Role.objects.get(id=int(t)))
        for t in team_two:
            banned_roles.append(Role.objects.get(id=int(t)))
        for role_o in team_one:
            current_role = Role.objects.get(id=role_o)
            best_matchups = WinRate.objects.filter(Q(role2=current_role) & ~Q(role1__in=banned_roles)).order_by('-win_rate')[0:5]
            if len(best_matchups) == 0:
                best_matchups = WinRate.objects.filter(Q(role1=current_role) & ~Q(role2__in=banned_roles)).order_by('-win_rate')[0:5]
            team_matchups.append(best_matchups)
            print(str(current_role) + ": " + str(best_matchups))

    final_data = {}

    for m in team_matchups:
        entry_line = []
        srole = ""
        for c in m:
            entry_line.append({"role_name": c.role1.name, "role1": c.role1.champion.name, "role2": c.role2.champion.name,
                               "portrait": c.role1.champion.portrait_image.name,
                               "win_rate": float(c.win_rate), "kills": int(c.role1.kills), "deaths": int(c.role1.deaths), "assists": int(c.role1.assists)})
            srole = str(c.role2.champion.name) + " as " + str(c.role2.name) 
        final_data[str(srole)] = entry_line

    return HttpResponse(json.dumps(final_data))


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

