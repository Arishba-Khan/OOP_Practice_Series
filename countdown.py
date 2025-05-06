# ------------------------------
# Countdown Iterator Example
# ------------------------------

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # Initialize the countdown value
        self.current = self.start
        return self

    def __next__(self):
        # Stop the loop when countdown goes below 0
        if self.current < 0:
            raise StopIteration

        # Save the current value to return
        value = self.current
        self.current -= 1  # Move to the next number
        return value

# ------------------------------
# Example Usage
# ------------------------------
if __name__ == "__main__":
    # Example 1: Use countdown in a for loop
    print("Countdown from 5:")
    for num in Countdown(5):
        print(num)

    # Example 2: Convert a countdown to a list
    countdown_list = list(Countdown(10))
    print(f"\nCountdown list from 10: {countdown_list}")

    # Example 3: Manual iteration using next()
    print("\nManual iteration from 3:")
    manual_countdown = Countdown(3)
    iterator = iter(manual_countdown)

    try:
        while True:
            value = next(iterator)
            print(value)
    except StopIteration:
        print("Countdown complete!")
