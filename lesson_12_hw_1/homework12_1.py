class Item:
    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"

class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.surname} {self.name}, {self.numberphone}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        output = f"Order for {self.user}:\n"
        for item, quantity in self.products.items():
            output += f"{item.name}: {quantity} pcs.\n"
        return output

    def get_total(self):
        total = 0
        for item, quantity in self.products.items():
            total += item.price * quantity
        return total

lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

print(lemon)  # lemon, price: 5
print(apple)  # apple, price: 2

buyer = User("Ivan", "Ivanov", "02628162")

cart = Purchase(buyer)
cart.add_item(lemon, 5)
cart.add_item(apple, 22)

print(cart)

print("Total amount: ", cart.get_total())
