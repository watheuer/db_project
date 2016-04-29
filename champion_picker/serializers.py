from rest_framework import serializers
from champion_picker.models import Champion, Role, WinRate, Item, ItemBuild

class RoleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role


class ChampionSerializer(serializers.ModelSerializer):
    roles = RoleDataSerializer(
        source='get_roles',
        read_only=True,
        many=True
    )

    class Meta:
        model = Champion
        fields = ('name', 'portrait_image', 'roles')


class RoleSerializer(serializers.ModelSerializer):
    champion = ChampionSerializer()

    class Meta:
        model = Role


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item


class BuildSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    role = RoleSerializer()

    class Meta:
        model = ItemBuild
