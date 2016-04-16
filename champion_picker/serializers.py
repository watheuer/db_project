from rest_framework import serializers
from models import Champion, Role, WinRate, Item, ItemBuild


class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = ('id', 'name', 'q_skill', 'w_skill', 'e_skill', 'r_skill')


class RoleSerializer(serializers.ModelSerializer):
    champion = ChampionSerializer()

    class Meta:
        model = Role
        fields = ('id', 'name', 'champion', 'win_rate', 'kills', 'deaths', 'assists', 'minions_killed')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item


class BuildSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    champion = ChampionSerializer()

    class Meta:
        model = ItemBuild
