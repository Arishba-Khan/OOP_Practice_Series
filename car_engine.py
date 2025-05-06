# Define the Engine class with its attributes and methods
class Engine:
    def __init__(self, engine_type):
        """Initialize the engine with type and status (off by default)."""
        self.engine_type = engine_type
        self.status = "off"
    
    def start(self):
        """Start the engine and set its status to 'on'."""
        self.status = "on"
        print(f"{self.engine_type} engine started")
    
    def stop(self):
        """Stop the engine and set its status to 'off'."""
        self.status = "off"
        print(f"{self.engine_type} engine stopped")
    
    def get_status(self):
        """Return the current status of the engine (on or off)."""
        return self.status

# Define the Car class with an engine composition
class Car:
    def __init__(self, brand, engine_type):
        """Initialize the car with brand and a specific engine."""
        self.brand = brand
        self.engine = Engine(engine_type)  # Car has an engine
    
    def start_car(self):
        """Start the car, which in turn starts the engine."""
        print(f"Starting {self.brand} car...")
        self.engine.start()
    
    def stop_car(self):
        """Stop the car, which in turn stops the engine."""
        print(f"Stopping {self.brand} car...")
        self.engine.stop()
    
    def check_engine_status(self):
        """Check and display the current status of the car's engine."""
        status = self.engine.get_status()
        print(f"{self.brand} car engine is {status}")

# Example usage
if __name__ == "__main__":
    # Create a car object with an engine type "V6"
    my_car = Car("Toyota", "V6")
    
    # Start the car (which starts the engine)
    my_car.start_car()
    
    # Check the engine status after starting the car
    my_car.check_engine_status()
    
    # Stop the car (which stops the engine)
    my_car.stop_car()
    
    # Check the engine status again after stopping the car
    my_car.check_engine_status()
