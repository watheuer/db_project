from rest_framework import serializers
from models import Champion, Role, WinRate, Item, ItemBuild


class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion


class RoleSerializer(serializers.ModelSerializer):
    champion = ChampionSerializer()

    class Meta:
        model = Role


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item


class BuildSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    champion = ChampionSerializer()

    class Meta:
        model = ItemBuild
