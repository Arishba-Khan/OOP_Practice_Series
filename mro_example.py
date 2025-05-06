# Base class A
class A:
    def show(self):
        print("Method from class A")

# Class B inherits from A and overrides show()
class B(A):
    def show(self):
        print("Method from class B")

# Class C also inherits from A and overrides show()
class C(A):
    def show(self):
        print("Method from class C")

# Class D inherits from both B and C (multiple inheritance)
class D(B, C):
    pass  # No show() method here, Python will use MRO to decide

# Example usage
if __name__ == "__main__":
    # Create instances of each class
    a = A()
    b = B()
    c = C()
    d = D()

    # Call show() method for each instance
    print("Calling show() on A instance:")
    a.show()  # Output: Method from class A

    print("\nCalling show() on B instance:")
    b.show()  # Output: Method from class B

    print("\nCalling show() on C instance:")
    c.show()  # Output: Method from class C

    print("\nCalling show() on D instance:")
    d.show()  # Output: Method from class B (due to MRO)

    # Display the Method Resolution Order (MRO)
    print("\nMethod Resolution Order for class D:")
    for cls in D.__mro__:
        print(cls)
