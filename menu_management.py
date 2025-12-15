def add_menu_item(menu, item):
    menu.append(item)
def remove_menu_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(item, "not found in menu")
def check_availability(menu, item):
    if item in menu:
        print(item, "is available")
    else:
        print(item, "is not available")
menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_menu_item(menu, "Tacos")
remove_menu_item(menu, "Salad")
check_availability(menu, "Pizza")
print("Updated menu:", menu)
