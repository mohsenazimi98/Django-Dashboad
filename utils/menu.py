from utils.menu_ids import APP_IDS

menu_registry = {}

def register_menu(label=None, app_id=None, parent=None):
    def decorator(func):
        nonlocal label
        display_name = label or func.__name__

        if app_id is None:
            app_id_local = func.__module__.split('.')[0]
        else:
            app_id_local = app_id

        if parent:
            if parent not in menu_registry:
                menu_registry[parent] = {
                    "label": APP_IDS.get(parent, parent),
                    "items": []
                }

            if not menu_registry[parent]["items"]:
                menu_registry[parent]["items"].append({
                    "name": parent,
                    "label": APP_IDS.get(parent, parent),
                    "url_name": "#",
                    "subitems": []
                })

            menu_registry[parent]["items"][0]["subitems"].append({
                "name": func.__name__,
                "label": display_name,
                "url_name": func.__name__,
            })

        else:  
            if app_id_local not in menu_registry:
                menu_registry[app_id_local] = {
                    "label": APP_IDS.get(app_id_local, app_id_local),
                    "items": []
                }

            menu_registry[app_id_local]["items"].append({
                "name": func.__name__,
                "label": display_name,
                "url_name": func.__name__,
                "subitems": []
            })

        return func
    return decorator
