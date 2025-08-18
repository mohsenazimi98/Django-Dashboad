# dashboard/context_processors.py
from utils.menu import menu_registry

def menu_items(request):
    return {"menu_registry": menu_registry}
