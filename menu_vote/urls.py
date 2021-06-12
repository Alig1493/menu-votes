"""menu_vote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import path, include

api_v1_patterns = [
    path("user/", include(arg=("menu_vote.users.urls", "user"), namespace="user")),
    path("restaurants/", include(arg=("menu_vote.restaurants.urls", "restaurants"), namespace="restaurants")),
    path("menus/", include(arg=("menu_vote.menus.urls", "menus"), namespace="menus"))
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(arg=(api_v1_patterns, "v1_patterns"), namespace="api_v1"))
]
