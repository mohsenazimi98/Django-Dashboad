from django.urls import path
from .views import *

urlpatterns = [
    path("", search, name="search"),
    path("2", search2, name="search2"),
]