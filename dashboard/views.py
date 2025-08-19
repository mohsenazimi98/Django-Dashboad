from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils.menu import register_menu
from utils.menu_ids import APP_IDS

@login_required
@register_menu(label="داشبورد", app_id="app_01")
def dashboard(request):

    context = {}
    return render(request, "dashboard/dashboard.html", context)