from manager import InventoryManager, Item

item1 = Item("Carrot", "Greens", 5, 1.00)
item2 = Item("Lettuce", "Greens", 3, 2.00)
item3 = Item("Carrot", "Greens", 2, 1.00)
manager = InventoryManager()
manager.view_all_items()
manager.add_item(item1)
manager.add_item(item2)
manager.add_item(item3)
print(manager.view_all_items())