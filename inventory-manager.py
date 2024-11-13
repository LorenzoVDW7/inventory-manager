class Item:
    def __init__(self, name, category, quantity, price):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def update_quantity(self, quantity: int):
        self.quantity = quantity

    def display_info(self):
        return (f"Name of the item: {self.name}."
                f"Category of the item {self.category}."
                f"Quantity of the category: {self.category}."
                f"Price of the item: {self.price}.")

    def update_price(self, price):
        self.price = price
