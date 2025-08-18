# dashboard/utils/menu.py
menu_registry = {}

def is_submenu(name=None):
    def decorator(func):
        app_name = func.__module__.split('.')[0]
        if app_name not in menu_registry:
            menu_registry[app_name] = []
        menu_registry[app_name].append({
            "name": name or func.__name__,
            "url_name": func.__name__
        })
        return func
    return decorator