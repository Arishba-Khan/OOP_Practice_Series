# -----------------------------------------
# Multiplier Class Using __call__ Method
# -----------------------------------------
class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Store the multiplication factor

    def __call__(self, x):
        """
        Makes the object callable like a function.
        Multiplies the input 'x' by the factor.
        """
        return x * self.factor

    def display_factor(self):
        """
        Displays the current multiplication factor.
        """
        return f"Current multiplication factor: {self.factor}"

# -----------------------------------------
# Example usage
# -----------------------------------------
if __name__ == "__main__":
    # Create a multiplier object with factor 5
    times5 = Multiplier(5)

    # Check if the object behaves like a function
    print(f"Is 'times5' callable? {callable(times5)}")  # True

    # Use the object to multiply 10 by 5
    result = times5(10)
    print(f"5 * 10 = {result}")

    # Display the multiplication factor
    print(times5.display_factor())

    # Create another multiplier with factor 2
    double = Multiplier(2)
    print(f"2 * 7 = {double(7)}")

    # Use the multiplier in a list comprehension
    numbers = [1, 2, 3, 4, 5]
    doubled = [double(n) for n in numbers]

    print(f"Original numbers: {numbers}")
    print(f"Doubled numbers: {doubled}")
