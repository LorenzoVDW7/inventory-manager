class Item:
    def __init__(self, name: str, category: str, quantity: int, price: float):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price * quantity

    def __str__(self):
        return (f"Item(name='{self.name}', category='{self.category}', "
                f"quantity={self.quantity}, total_price={self.price:.2f})")


    def display_info(self) -> str:
        """Displays the complete item information."""
        return (f"Name of the item: {self.name}.\n"
                f"Category of the item {self.category}.\n"
                f"Quantity of the category: {self.category}.\n"
                f"Price of the item: {self.price}.")

    def update_price(self, price) -> None:
        """Updates the price of the item."""
        self.price = price

    def update_quantity(self, quantity) -> None:
        """Updates the quantity of the item."""
        self.quantity = quantity


class InventoryManager:
    def __init__(self):
        self.inventory = []

    def __str__(self):
        return "\n".join(str(item) for item in self.inventory)

    def add_item(self, item) -> None:
        """Adds item to the inventory, based on item details."""
        if item.name not in self.inventory:
            self.inventory.append(item)
        else:
            index = self.inventory.index(item)
            self.inventory[index].quantity += item.quantity

    def view_all_items(self) -> str:
        """Returns a string representation of all items in the inventory."""
        if not self.inventory:
            return "Inventory is empty."
        return "\n".join(str(item) for item in self.inventory)

    def remove_item(self, item) -> bool:
        """If specified item is found in inventory, remove this item from inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} was removed from the inventory.")
            return True
        return False
