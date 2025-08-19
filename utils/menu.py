# # dashboard/utils/menu.py
# menu_registry = {}

# def is_submenu(name=None):
#     def decorator(func):
#         app_name = func.__module__.split('.')[0]
#         if app_name not in menu_registry:
#             menu_registry[app_name] = []
#         menu_registry[app_name].append({
#             "name": name or func.__name__,
#             "url_name": func.__name__
#         })
#         return func
#     return decorator

# dashboard/utils/menu.py
menu_registry = {}

def register_menu(app_name=None, label=None, parent=None):
    """
    ثبت آیتم منو یا زیرمنو
    - app_name: نام اپ (یا نام منو اصلی)
    - label: اسم نمایشی
    - parent: اگر None باشد خودش منو اصلی است،
              اگر مقدار داشته باشد، زیرمنوی آن است.
    """
    def decorator(func):
        nonlocal app_name, label
        app = app_name or func.__module__.split('.')[0]
        display_name = label or func.__name__

        if app not in menu_registry:
            menu_registry[app] = {"label": app, "items": []}

        if parent:  # یعنی زیرمنو
            # پیدا کردن منوی والد
            parent_menu = next(
                (m for m in menu_registry[app]["items"] if m["name"] == parent),
                None
            )
            if not parent_menu:
                parent_menu = {"name": parent, "label": parent, "subitems": []}
                menu_registry[app]["items"].append(parent_menu)

            parent_menu["subitems"].append({
                "name": func.__name__,
                "label": display_name,
                "url_name": func.__name__,
            })
        else:  # یعنی خودش منو اصلیه
            menu_registry[app]["items"].append({
                "name": func.__name__,
                "label": display_name,
                "url_name": func.__name__,
                "subitems": []
            })
        return func
    return decorator
