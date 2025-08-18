from django.shortcuts import render
from utils.menu import is_submenu

@is_submenu(name="زیرمنو اول")
def search(request):
   
    context = {
    }
    return render(request, "app_search/search.html", context)

@is_submenu(name="زیرمنو دوم")
def search2(request):
   
    context = {
    }
    return render(request, "app_search/search2.html", context)
