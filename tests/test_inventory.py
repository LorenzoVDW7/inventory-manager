import pytest

from manager import InventoryManager, Item

def test_create_item():
    item1 = Item("Broccoli", "Vegetables", 18, 1.18)
    assert item1.name == "Broccoli"
    assert item1.price == 1.18
    assert item1.quantity == 18
