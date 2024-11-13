class Item:
    def __init__(self, name: str, category: str, quantity: int, price: float):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def update_quantity(self, quantity: int) -> None:
        """Updates the quantity of the item."""
        self.quantity = quantity

    def display_info(self) -> str:
        """Displays the complete item information."""
        return (f"Name of the item: {self.name}."
                f"Category of the item {self.category}."
                f"Quantity of the category: {self.category}."
                f"Price of the item: {self.price}.")

    def update_price(self, price) -> None:
        """Updates the price of the item."""
        self.price = price

class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        """Adds item to the inventory, based on item details."""
        item = Item(item.name, item.category, item.quantity, item.price)
        self.inventory.append(item)

    def view_all_items(self) -> list:
        """If items are found in inventory, returns list of items."""
        if not self.inventory:
            raise ValueError("Inventory is empty.")
        return self.inventory

    def remove_item(self, item) -> bool:
        """If specified item is found in inventory, remove this item from inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} was removed from the inventory.")
            return True
        return False
