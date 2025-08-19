from django.shortcuts import render
from utils.menu import register_menu


@register_menu(label="داشبورد")
def dashboard(request):

    context = {}
    return render(request, "dashboard/dashboard.html", context)