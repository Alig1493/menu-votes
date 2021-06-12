from django.db import models

from menu_vote.base.models import TimeStampedModel
from menu_vote.menus.utils import menu_upload_path


class Menu(TimeStampedModel):
    restaurant = models.ForeignKey("restaurants.Restaurant", on_delete=models.CASCADE, related_name="menus")
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to=menu_upload_path)
