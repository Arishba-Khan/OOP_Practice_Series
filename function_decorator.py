import time
import functools

# ----------------------------
# Simple decorator to log calls
# ----------------------------
def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is being called.")
        return func(*args, **kwargs)
    return wrapper

# --------------------------------------------
# Decorator that repeats a function n times
# --------------------------------------------
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                print(f"Repetition {i + 1} of '{func.__name__}'")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# ----------------------------------------
# Decorator to measure execution time
# ----------------------------------------
def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.6f} seconds to run.")
        return result
    return wrapper

# -------------------------------------
# Functions using the above decorators
# -------------------------------------

@log_function_call
def say_hello(name):
    return f"Hello, {name}!"

@repeat(3)
def say_hi(name):
    print(f"Hi, {name}!")
    return f"Hi, {name}!"

@timing_decorator
def slow_function():
    time.sleep(1)  # Simulates a time-consuming task
    return "Function completed"

# -----------------------
# Example usage
# -----------------------
if __name__ == "__main__":
    # Log decorator in action
    print("\nCalling say_hello:")
    result = say_hello("Alice")
    print(result)

    # Repeat decorator in action
    print("\nCalling say_hi with repetition:")
    say_hi("Bob")

    # Timing decorator in action
    print("\nCalling slow_function with timer:")
    result = slow_function()
    print(result)
