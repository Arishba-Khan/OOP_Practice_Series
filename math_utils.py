# Define the MathUtils class to handle basic mathematical operations
class MathUtils:
    
    @staticmethod
    def add(a, b):
        """
        Add two numbers.
        :param a: First number
        :param b: Second number
        :return: Sum of a and b
        """
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """
        Subtract the second number from the first.
        :param a: First number
        :param b: Second number
        :return: Difference between a and b
        """
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """
        Multiply two numbers.
        :param a: First number
        :param b: Second number
        :return: Product of a and b
        """
        return a * b
    
    @staticmethod
    def divide(a, b):
        """
        Divide the first number by the second. Returns an error message if dividing by zero.
        :param a: First number
        :param b: Second number
        :return: Quotient of a and b, or an error message if dividing by zero
        """
        if b == 0:
            return "Cannot divide by zero"
        return a / b

# Example usage: Demonstrating basic math operations using the MathUtils class
if __name__ == "__main__":
    # Using static methods without creating an instance of MathUtils
    print(f"5 + 3 = {MathUtils.add(5, 3)}")      # Output: 8
    print(f"10 - 4 = {MathUtils.subtract(10, 4)}")  # Output: 6
    print(f"6 * 7 = {MathUtils.multiply(6, 7)}")  # Output: 42
    print(f"20 / 5 = {MathUtils.divide(20, 5)}")  # Output: 4.0
    print(f"10 / 0 = {MathUtils.divide(10, 0)}")  # Output: Cannot divide by zero
