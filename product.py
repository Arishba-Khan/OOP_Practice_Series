# -------------------------------
# Product Class with Price Control
# -------------------------------
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Protected attribute (by convention)

    # -------------------
    # Getter for price
    # -------------------
    @property
    def price(self):
        return self._price

    # -------------------
    # Setter for price
    # -------------------
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    # -------------------
    # Deleter for price
    # -------------------
    @price.deleter
    def price(self):
        print(f"Deleting price for product: {self.name}")
        self._price = 0

# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    # Create a Product object
    laptop = Product("Laptop", 999.99)

    # Access price using the getter
    print(f"Product: {laptop.name}, Price: ${laptop.price}")

    # Update price using the setter
    laptop.price = 899.99
    print(f"Updated Price: ${laptop.price}")

    # Try setting a negative price (should raise an error)
    try:
        laptop.price = -100
    except ValueError as e:
        print(f"Error: {e}")

    # Delete price using the deleter
    del laptop.price
    print(f"Price after deletion: ${laptop.price}")
