from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils.menu import register_menu
from utils.menu_ids import APP_IDS

@login_required
@register_menu(label="جستجو عادی", parent="app_02")
def search(request):
   
    context = {
    }
    return render(request, "app_search/search.html", context)

@login_required
@register_menu(label="جستجو پیشرفته", parent="app_02")
def search2(request):
   
    context = {
    }
    return render(request, "app_search/search2.html", context)
