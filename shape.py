from abc import ABC, abstractmethod
import math

# Abstract base class for Shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass

# Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        """
        Initializes a rectangle with a given width and height.
        :param width: The width of the rectangle
        :param height: The height of the rectangle
        """
        self.width = width
        self.height = height
    
    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

# Circle class that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        """
        Initializes a circle with a given radius.
        :param radius: The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculates and returns the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

# Example usage
if __name__ == "__main__":
    # Attempt to instantiate the abstract base class (this will raise an error)
    try:
        shape = Shape()  # This line will raise a TypeError because Shape is abstract
    except TypeError as e:
        print(f"Error: {e}")
    
    # Create a Rectangle object and calculate its area and perimeter
    rectangle = Rectangle(5, 3)
    print(f"Rectangle area: {rectangle.area()}")
    print(f"Rectangle perimeter: {rectangle.perimeter()}")
    
    # Create a Circle object and calculate its area and perimeter
    circle = Circle(4)
    print(f"Circle area: {circle.area():.2f}")
    print(f"Circle perimeter: {circle.perimeter():.2f}")
