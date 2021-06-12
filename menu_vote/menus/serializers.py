from drf_extra_fields.fields import HybridImageField
from rest_framework import serializers

from menu_vote.menus.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    image = HybridImageField()

    class Meta:
        model = Menu
        fields = ["id", "restaurant", "name", "image"]
