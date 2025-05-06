# Employee class to demonstrate public, protected, and private variables and methods
class Employee:
    def __init__(self, name, salary, ssn):
        """
        Initializes an Employee instance with name, salary, and SSN.
        :param name: The employee's name
        :param salary: The employee's salary
        :param ssn: The employee's Social Security Number (SSN)
        """
        self.name = name          # Public variable (accessible directly)
        self._salary = salary     # Protected variable (conventionally protected, but accessible)
        self.__ssn = ssn          # Private variable (name mangled to make it less accessible)
    
    def display_info(self):
        """Displays employee details."""
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")
    
    def _protected_method(self):
        """A protected method (should not be accessed directly outside the class)."""
        print("This is a protected method")
    
    def __private_method(self):
        """A private method (should not be accessed directly outside the class)."""
        print("This is a private method")
    
    def access_private_method(self):
        """A public method to access the private method indirectly."""
        self.__private_method()

# Example usage: Demonstrating the Employee class and its variable accessibility
if __name__ == "__main__":
    # Create an employee object
    emp = Employee("John Doe", 75000, "123-45-6789")
    
    # Access public variable directly
    print(f"Public - Name: {emp.name}")
    
    # Access protected variable directly (possible but not recommended)
    print(f"Protected - Salary: {emp._salary}")
    
    # Try to access private variable directly (this will cause an error)
    try:
        print(f"Private - SSN: {emp.__ssn}")
    except AttributeError as e:
        print(f"Error: {e}")  # Error: 'Employee' object has no attribute '__ssn'
    
    # Access private variable via name mangling (name mangling is used to make private variables harder to access)
    try:
        print(f"Private (via name mangling) - SSN: {emp._Employee__ssn}")
    except AttributeError as e:
        print(f"Error: {e}")
    
    # Call the display_info method to show all employee details
    emp.display_info()
    
    # Call protected method directly (possible but not recommended)
    emp._protected_method()  
    
    # Try to call private method directly (this will cause an error)
    try:
        emp.__private_method()
    except AttributeError as e:
        print(f"Error: {e}")  # Error: 'Employee' object has no attribute '__private_method'
    
    # Call private method indirectly via a public method
    emp.access_private_method()
