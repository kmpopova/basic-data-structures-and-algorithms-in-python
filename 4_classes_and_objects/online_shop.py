import random

"""
Objective:

*   Practice creating classes and objects.
*   Design and implement a class hierarchy (multiple related classes).
*   Apply encapsulation (hiding data within a class).
*   (Optional) Implement inheritance and polymorphism.

Project: Simple E-commerce System

Goal: Build a simplified e-commerce system with the following classes:

1.  **`Product` Class:**
2.  **`Category` Class:**
3.  **`ShoppingCart` Class:**
    
"""

class Product:

    """
**`Product` Class:**
    *   **Attributes:**
        *   `name` (string)
        *   `price` (float)
        *   `description` (string)
        *   `product_id` (integer, you can generate this automatically, 
        or ask the user to input it, but it has to be unique.)
    *   **Methods:**
        *   `__init__(self, name, price, description, product_id)`: 
        The constructor.
        *   `get_details(self)`: Returns a string with the product's name, 
        price, and description.

"""

    def __init__(self, name: str, price: float, description: str, product_id: int):
        self.name = name
        self.price = price
        self.description = description
        if product_id != None:
            self.product_id = product_id
        else:
            user_provided_ID = input("Please enter the Product ID:")
            if user_provided_ID != None and user_provided_ID != "":
                self.product_id = user_provided_ID
            else:
                self.product_id = random.randint(1, 1000)


    def get_details(self):
        return f"Product: {self.name}, Price: ${self.price}, Description: {self.description}"
    
    def apply_discount(self, discount=0.1):
        self.price -= round(self.price*discount, 2)
    
class ElectronicProduct(Product):

    """
    A child class of Product, with a differently defined apply_discount() method.
    """

    def __init__(self, name, price, description, product_id, warranty=12):
        super().__init__(name, price, description, product_id)
        self.warranty = warranty

    def apply_discount(self, discount=0.1):
        """
        Depending on warranty, a different discount is applied.
        """
        if self.warranty >= 12:
            super().apply_discount(discount)
        else:
            super().apply_discount(discount*2)
            #self.price -= round(self.price*discount*2, 2)
         

class Category:

    """
**`Category` Class:**
    *   **Attributes:**
        *   `name` (string)
        *   `description` (string, optional)
        *   `products` (list, initially empty)
    *   **Methods:**
        *   `__init__(self, name, description="")`: The constructor.
        *   `add_product(self, product)`: Adds a `Product` object to the `products` list.
        *   `get_products(self)`: Returns the list of products in the category.
        *   `get_category_details(self)`: Returns a string with the category's name 
        and description (you can also list the products if you want to make it more 
        interesting).
"""
    
    def __init__(self, name: str, description=""):
        self.name = name
        self.products = []
        self.description = description

    def add_product(self, product: Product):
        self.products.append(product)

    def get_products(self):
        return self.products
    
    def get_category_details(self):
        return f"Category {self.name}, {self.description}, contains the following products: {[product.name for product in self.products]}."


class ShoppingCart:

    """
**`ShoppingCart` Class:**
    *   **Attributes:**
        *   `items` (dictionary, keys are `Product` objects, values are quantities)
    *   **Methods:**
        *   `__init__(self)`: The constructor.
        *   `add_item(self, product, quantity=1)`: Adds a `Product` to the cart, 
        increasing the quantity if it already exists.
        *   `remove_item(self, product, quantity=1)`: Removes a specified quantity of 
        a product from the cart. If the quantity to remove exceeds the quantity in the cart, 
        remove the product from the cart.
        *   `calculate_total(self)`: Calculates and returns the total cost of all items 
        in the cart.
        *   `display_cart(self)`: Displays the items in the cart (product name and quantity) 
        and the total cost.
"""

    def __init__(self):
        self.items = {}

    def add_item(self, product: Product, quantity=1):
        self.items[product] = quantity

    def remove_item(self, product: Product, quantity=1):
        if quantity > 0:
            if product in self.items:
                if self.items[product]-quantity <= 0:
                    self.items.pop(product)
                    print(f"All {product.name}s removed from your cart.")
                else:
                    self.items[product] -= quantity
                    print(f"{quantity} {product.name} removed from your cart.")
            else:
                print(f"Nothing to remove. You do not have {product.name} in your cart.")
        else:
            print("The number of items to remove must be a positive number.")


    def calculate_total(self):
       return sum(product.price for product in self.items.keys())

    def display_cart(self):
        print("Your shopping cart contains:")
        for product in self.items:
            print(f"{self.items[product]} {product.name}")
        print(f"The total cost of items in your cart is ${self.calculate_total()}")

        
if __name__ == "__main__":

    computer = Product("Computer #1", 1999.99, "A basic desktop computer", 1)
    print(computer.get_details())
    mouse = Product("Mouse #1", 22.99, "a computer mouse", 2)
    table = Product("Writing table", 59.99, "The perfect computer table", 3)
    print(table.price)
    table.apply_discount()
    print(table.price)

    old_computer = ElectronicProduct("Second-hand computer", 599.99, "a second-hand computer", 5, 6)
    print(old_computer.price)
    old_computer.apply_discount()
    print(old_computer.price)

    old_computer2 = Product("Second-hand computer", 599.99, "another second hand computer", 4)
    print(old_computer2.price)
    old_computer2.apply_discount()
    print(old_computer2.price)

    my_shopping_cart = ShoppingCart()
    my_shopping_cart.add_item(computer)
    my_shopping_cart.add_item(mouse)
    my_shopping_cart.add_item(table)
    my_shopping_cart.display_cart()
    my_shopping_cart.remove_item(computer, -6)
    my_shopping_cart.remove_item(computer, 0)
    my_shopping_cart.remove_item(computer, 7)
    print(f"The cotal cost of all items in your shopping cart is: ${my_shopping_cart.calculate_total()}")

    electronic_products = Category("Electronic products", "Products like computer and mouse")
    electronic_products.add_product(computer)
    electronic_products.add_product(mouse)
    print(electronic_products.get_category_details())

    my_shopping_cart.display_cart()