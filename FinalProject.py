# Carlos Arriola
# Final Project
# December 13, 2023
class ItemToPurchase:
    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

    def get_item_price(self):
        return self.item_price

    def get_item_quantity(self):
        return self.item_quantity

    def set_item_quantity(self, quantity):
        self.item_quantity = quantity

    def get_item_cost(self):
        return self.item_price * self.item_quantity

    def get_item_name(self):
        return self.item_name


class ShoppingCart:
    def __init__(self, name="none", date="January 1, 2016", catalog=None):
        if catalog is None:
            catalog = {}
        self.customer_name = name
        self.current_date = date
        self.cart_items = catalog

    def add_item(self, name, item):
        self.cart_items.update({name: item})
        print(f"{name} successfully added.\n")

    def remove_item(self, item):
        try:
            del self.cart_items[item]
            print(f"{item} successfully removed.\n")
        except KeyError:
            print("Item not found in cart. Nothing removed.\n")

    def modify_item(self, item, quantity):
        if item in self.cart_items:
            self.cart_items[item].set_item_quantity(quantity)
            print(f"{item} successfully modified.\n")
        else:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return len(self.cart_items)

    def get_cost_of_cart(self):
        total = 0.0
        for item in self.cart_items:
            total += self.cart_items[item].get_item_cost()
        return total

    def print_total(self):
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        for item in self.cart_items:
            self.cart_items[item].print_item_cost()
        print(f"\nTotal: ${self.get_cost_of_cart():.2f}\n")

    def print_descriptions(self):
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"\nItem Descriptions")
        for item in self.cart_items:
            self.cart_items[item].print_item_description()
        print("")


def print_menu():
    print("MENU"
          "\na - Add item to cart"
          "\nr - Remove item from cart"
          "\nc - Change item quantity"
          "\ni - Output items' descriptions"
          "\no - Output shopping cart"
          "\nq - Quit")


def execute_menu(choice, shopping_cart):
    if choice == 'a':
        print("\nADD ITEM TO CART")
        name = input("Enter the item name: ")
        description = input("Enter the item description: ")
        price = float(input("Enter the item price: $"))
        quantity = int(input("Enter the item quantity: "))
        item = ItemToPurchase(name, price, quantity, description)
        shopping_cart.add_item(name, item)
    elif choice == 'r':
        print("\nREMOVE ITEM FROM CART")
        item_name = input("Enter name of item to remove: ")
        shopping_cart.remove_item(item_name)
    elif choice == 'c':
        print("\nCHANGE ITEM QUANTITY")
        item = input("Enter the item name: ")
        quantity = int(input("Enter the new quantity: "))
        shopping_cart.modify_item(item, quantity)
    elif choice == 'i':
        shopping_cart.print_descriptions()
    elif choice == 'o':
        shopping_cart.print_total()
    elif choice == 'q':
        print("\nQUIT")
        exit(0)
    else:
        print("Choice unknown, try again.")


def main():
    name = input("Enter customer's name: ")
    date = input("Enter today's date: ")

    print(f"\nCustomer name: {name}")
    print(f"Today's date: {date}\n")

    shopping_cart = ShoppingCart(name, date)
    while True:
        print_menu()
        choice = input("Make a selection: ")
        execute_menu(choice, shopping_cart)


if __name__ == "__main__":
    main()
