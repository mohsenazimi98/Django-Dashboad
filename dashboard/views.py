from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils.menu import register_menu

@login_required
@register_menu(label="داشبورد")
def dashboard(request):

    context = {}
    return render(request, "dashboard/dashboard.html", context)