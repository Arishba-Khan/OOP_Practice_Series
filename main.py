# Import all necessary classes from different modules
from student import Student
from counter import Counter
from car import Car
from bank import Bank
from math_utils import MathUtils
from logger import Logger
from employee import Employee
from person_teacher import Person, Teacher
from shape import Rectangle, Circle
from dog import Dog
from book import Book
from temperature_converter import TemperatureConverter
from car_engine import Car as CompositionCar, Engine
from department_employee import Department, Employee as AggregationEmployee
from mro_example import A, B, C, D
from function_decorator import say_hello, say_hi, slow_function
from class_decorator import Person as DecoratedPerson, Car as CountedCar
from product import Product
from multiplier import Multiplier
from custom_exception import check_age, InvalidAgeError
from countdown import Countdown

# Main function to test all classes
def main():
    # ===== Testing Student Class =====
    print("\n===== Testing Student Class =====")
    student = Student("Alice", 95)
    student.display()

    # ===== Testing Counter Class =====
    print("\n===== Testing Counter Class =====")
    c1 = Counter()
    c2 = Counter()
    Counter.display_count()

    # ===== Testing Car Class =====
    print("\n===== Testing Car Class =====")
    my_car = Car("Toyota")
    print(f"Car brand: {my_car.brand}")
    my_car.start()

    # ===== Testing Bank Class =====
    print("\n===== Testing Bank Class =====")
    branch = Bank("Downtown")
    branch.display_details()
    Bank.change_bank_name("City Bank")
    branch.display_details()

    # ===== Testing MathUtils Class =====
    print("\n===== Testing MathUtils Class =====")
    print(f"5 + 3 = {MathUtils.add(5, 3)}")
    print(f"10 - 4 = {MathUtils.subtract(10, 4)}")

    # ===== Testing Logger Class =====
    print("\n===== Testing Logger Class =====")
    logger = Logger("TestLogger")
    logger.log("This is a test message")

    # ===== Testing Employee Class =====
    print("\n===== Testing Employee Class =====")
    emp = Employee("John Doe", 75000, "123-45-6789")
    emp.display_info()

    # ===== Testing Person and Teacher Classes =====
    print("\n===== Testing Person and Teacher Classes =====")
    teacher = Teacher("Mr. Smith", 45, "Mathematics")
    teacher.display_info()

    # ===== Testing Shape Classes =====
    print("\n===== Testing Shape Classes =====")
    rectangle = Rectangle(5, 3)
    print(f"Rectangle area: {rectangle.area()}")
    circle = Circle(4)
    print(f"Circle area: {circle.area():.2f}")

    # ===== Testing Dog Class =====
    print("\n===== Testing Dog Class =====")
    dog = Dog("Buddy", "Golden Retriever")
    dog.bark()
    dog.play("fetch")

    # ===== Testing Book Class =====
    print("\n===== Testing Book Class =====")
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    Book.display_total_books()

    # ===== Testing TemperatureConverter Class =====
    print("\n===== Testing TemperatureConverter Class =====")
    celsius = 25
    fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit:.2f}°F")

    # ===== Testing Composition (Car and Engine) =====
    print("\n===== Testing Composition =====")
    car = CompositionCar("Toyota", "V6")
    car.start_car()
    car.check_engine_status()

    # ===== Testing Aggregation (Employee and Department) =====
    print("\n===== Testing Aggregation =====")
    emp1 = AggregationEmployee("John Doe", "E001")
    dept = Department("Human Resources")
    dept.add_employee(emp1)
    dept.display_employees()

    # ===== Testing MRO (Method Resolution Order) =====
    print("\n===== Testing MRO =====")
    d = D()
    d.show()
    print(f"MRO for class D: {D.__mro__}")

    # ===== Testing Function Decorators =====
    print("\n===== Testing Function Decorators =====")
    result = say_hello("Alice")
    print(result)

    # ===== Testing Class Decorators =====
    print("\n===== Testing Class Decorators =====")
    person = DecoratedPerson("John")
    print(person.greet())

    # ===== Testing Property Decorators =====
    print("\n===== Testing Property Decorators =====")
    product = Product("Laptop", 999.99)
    print(f"Product: {product.name}, Price: ${product.price}")

    # ===== Testing __call__ (Multiplier) =====
    print("\n===== Testing __call__ =====")
    times5 = Multiplier(5)
    print(f"5 * 10 = {times5(10)}")

    # ===== Testing Custom Exception =====
    print("\n===== Testing Custom Exception =====")
    try:
        result = check_age(25)
        print(result)
    except InvalidAgeError as e:
        print(f"Error: {e}")

    # ===== Testing Custom Iterable (Countdown) =====
    print("\n===== Testing Custom Iterable =====")
    countdown = Countdown(5)
    print("Countdown:")
    for num in countdown:
        print(num)

# Ensure the main function runs only when this file is executed directly
if __name__ == "__main__":
    main()
