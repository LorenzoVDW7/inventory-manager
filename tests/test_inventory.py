import pytest

from manager import InventoryManager, Item

def test_create_item():
    item1 = Item("Broccoli", "Vegetables", 18, 1.18)
    assert item1.name == "Broccoli"
    assert item1.price == 1.18
    assert item1.quantity == 18

def test_update_price():
    item1 = Item("Broccoli", "Vegetables", 18, 1.18)
    item1.update_price(1.40)
    assert item1.price == 1.40

def test_update_quantity():
    item1 = Item("Broccoli", "Vegetables", 18, 1.18)
    item1.update_quantity(3)
    assert item1.quantity == 3

def test_empty_inventory():
    manager = InventoryManager()
    manager.inventory = None
    assert manager.view_all_items() == []

def test_add_item_to_inventory():
    manager = InventoryManager()
    item1 = Item("Broccoli", "Vegetables", 18, 1.18)
    manager.add_item(item1)
    assert manager.view_all_items() != []

def test_remove_item_from_inventory():
    manager = InventoryManager()
    assert manager.view_all_items() == []
    item1 = Item("Broccoli", "Vegetables", 18, 1.18)
    manager.add_item(item1)
    assert manager.view_all_items() != []
    manager.remove_item(item1)
    assert manager.view_all_items() == []


