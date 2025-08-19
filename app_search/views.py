from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils.menu import register_menu

@login_required
@register_menu(label="جستجو عادی", parent="جستجو")
def search(request):
   
    context = {
    }
    return render(request, "app_search/search.html", context)

@login_required
@register_menu(label="جستجو پیشرفته", parent="جستجو")
def search2(request):
   
    context = {
    }
    return render(request, "app_search/search2.html", context)
