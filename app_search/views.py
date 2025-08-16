from django.shortcuts import render

def search(request):
   
    context = {
    }
    return render(request, "app_search/search.html", context)
