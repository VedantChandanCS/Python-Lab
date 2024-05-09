class Restaurant:
    def __init__(self, name, cuisine, rating, dishes, payment_methods, discount):
        self.name = name
        self.cuisine = cuisine
        self.rating = rating
        self.dishes = dishes
        self.payment_methods = payment_methods
        self.discount = discount

    def display_details(self):
        print("Restaurant Details:")
        print("Name:", self.name)
        print("Cuisine:", self.cuisine)
        print("Rating:", self.rating)

    def display_dishes(self):
        print("\nAvailable Dishes:")
        for dish, price in self.dishes.items():
            print(f"{dish}: ${price}")

    def display_payment_methods(self):
        print("\nAccepted Payment Methods:")
        for method in self.payment_methods:
            print(method)

    def apply_discount(self, total_amount):
        discount_amount = total_amount * (self.discount / 100)
        final_amount = total_amount - discount_amount
        return final_amount

    def show_bill(self, ordered_items):
        total_bill = 0
        print("\nYour Bill:")
        for item, quantity in ordered_items.items():
            price = self.dishes.get(item, 0)
            item_total = price * quantity
            total_bill += item_total
            print(f"{item}: ${price} x {quantity} = ${item_total}")

        if self.discount > 0:
            final_bill = self.apply_discount(total_bill)
            print(f"\nTotal Bill (After {self.discount}% Discount): ${final_bill}")
        else:
            print(f"\nTotal Bill: ${total_bill}")


# Create an object of the Restaurant class
restaurant1 = Restaurant(
    "La Pizzeria",
    "Italian",
    4.5,
    {
        "Margherita Pizza": 10,
        "Pasta Carbonara": 12,
        "Tiramisu": 6
    },
    ["Cash", "Credit Card", "Digital Wallet"],
    10  # 10% discount
)

# Accessing and printing details of the object
print("Details of Restaurant Object:")
restaurant1.display_details()
restaurant1.display_dishes()
restaurant1.display_payment_methods()

# Ordering some dishes
ordered_items = {
    "Margherita Pizza": 2,
    "Tiramisu": 1
}

# Showing the bill
restaurant1.show_bill(ordered_items)
