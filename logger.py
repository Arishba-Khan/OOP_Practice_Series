# Logger class to handle logging messages with a specific name
class Logger:
    def __init__(self, name):
        """
        Initialize the Logger instance with a name.
        :param name: Name of the logger instance
        """
        self.name = name
        print(f"Logger '{self.name}' has been created")

    def log(self, message):
        """
        Log a message with the format: [LoggerName] message.
        :param message: The message to log
        """
        print(f"[{self.name}] {message}")
    
    def __del__(self):
        """
        Destructor method to print when the logger instance is being destroyed.
        """
        print(f"Logger '{self.name}' is being destroyed")

# Example usage: Demonstrating how the Logger class works
if __name__ == "__main__":
    # Create a logger instance with the name 'AppLogger'
    app_logger = Logger("AppLogger")
    
    # Use the app_logger to log messages
    app_logger.log("Application started")
    app_logger.log("Processing data")
    
    # Create another logger instance with the name 'SystemLogger'
    system_logger = Logger("SystemLogger")
    system_logger.log("System check completed")
    
    # Explicitly delete the first logger (app_logger)
    print("Deleting app_logger...")
    del app_logger  # Destructor (__del__) will be called here
    
    # The second logger (system_logger) will be destroyed when the program ends
    print("Program ending...")
