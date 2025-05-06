# Counter class definition
class Counter:
    # Class variable to keep track of the total count of objects created
    count = 0
    
    def __init__(self):
        # Increment the class variable count every time a new object is created
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        # Display the total count of objects created
        print(f"Total number of Counter objects created: {cls.count}")
    
    @classmethod
    def reset_count(cls):
        # Reset the count to 0 and notify the user
        cls.count = 0
        print("Counter has been reset to 0")

# Main block to demonstrate class functionality
if __name__ == "__main__":
    # Creating multiple Counter objects
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()
    
    # Display the total number of Counter objects created
    Counter.display_count()  # Output: Total number of Counter objects created: 3
    
    # Creating more Counter objects
    c4 = Counter()
    c5 = Counter()
    
    # Display the updated count
    Counter.display_count()  # Output: Total number of Counter objects created: 5
    
    # Reset the count to 0
    Counter.reset_count()
    
    # Display the count after resetting
    Counter.display_count()  # Output: Total number of Counter objects created: 0
