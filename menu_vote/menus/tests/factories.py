from factory import DjangoModelFactory, SubFactory, Faker
from factory.django import ImageField

from menu_vote.menus.models import Menu
from menu_vote.restaurants.tests.factories import RestaurantFactory


class MenuFactory(DjangoModelFactory):
    restaurant = SubFactory(RestaurantFactory)
    name = Faker("name")
    image = ImageField()

    class Meta:
        model = Menu
