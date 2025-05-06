# ------------------------------
# Custom Exception Example
# ------------------------------

# Define a custom exception for invalid age
class InvalidAgeError(Exception):
    """Raised when age is below the minimum allowed."""

    def __init__(self, age, message="Age is below the minimum required age"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.age} (minimum age is 18)"

# Function that checks age and raises the custom exception if needed
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)  # Raise the custom exception
    return f"Age {age} is valid"

# ------------------------------
# Example Usage
# ------------------------------
if __name__ == "__main__":
    # ✅ Case 1: Valid age
    try:
        result = check_age(25)
        print(result)
    except InvalidAgeError as e:
        print(f"Error: {e}")

    # ❌ Case 2: Invalid age (below 18)
    try:
        result = check_age(15)
        print(result)
    except InvalidAgeError as e:
        print(f"Error: {e}")

    # ❌ Case 3: Invalid age with a custom message
    try:
        age = 16
        if age < 18:
            raise InvalidAgeError(age, "Voting requires minimum age")
        print(f"You can vote at age {age}")
    except InvalidAgeError as e:
        print(f"Error: {e}")
