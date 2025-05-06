# ------------------------------
# Class decorator to add a greet method
# ------------------------------
def add_greeting(cls):
    # Adds a method called 'greet' to any class it decorates
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

# -----------------------------------
# Class decorator to count instances
# -----------------------------------
def count_instances(cls):
    # Save the original __init__ method
    original_init = cls.__init__

    # Define a new __init__ that counts instances
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        if not hasattr(cls, 'instance_count'):
            cls.instance_count = 0
        cls.instance_count += 1

    # Replace the original __init__ with the new one
    cls.__init__ = new_init

    # Add a class method to get the instance count
    cls.get_instance_count = classmethod(lambda cls: cls.instance_count)
    return cls

# ------------------------------
# Apply decorator to Person class
# ------------------------------
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        return f"My name is {self.name}"

# ------------------------------
# Apply decorator to Car class
# ------------------------------
@count_instances
class Car:
    def __init__(self, brand):
        self.brand = brand

    def get_brand(self):
        return f"This car is a {self.brand}"

# ------------------------------
# Example usage
# ------------------------------
if __name__ == "__main__":
    # Person class has a new method 'greet'
    print("Testing Person class with @add_greeting:")
    person = Person("John")
    print(person.say_name())
    print(person.greet())  # Method added by decorator

    print("\nTesting Car class with @count_instances:")
    car1 = Car("Toyota")
    car2 = Car("Honda")
    car3 = Car("Ford")

    # Display brand and count
    print(car1.get_brand())
    print(f"Number of Car instances: {Car.get_instance_count()}")

    # Create another Car object
    car4 = Car("BMW")
    print(f"After adding another car, count: {Car.get_instance_count()}")
