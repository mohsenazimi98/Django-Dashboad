from django.shortcuts import render
from utils.menu import register_menu

@register_menu(label="جستجو عادی", parent="جستجو")
def search(request):
   
    context = {
    }
    return render(request, "app_search/search.html", context)

@register_menu(label="جستجو پیشرفته", parent="جستجو")
def search2(request):
   
    context = {
    }
    return render(request, "app_search/search2.html", context)
