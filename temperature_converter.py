class TemperatureConverter:
    # Static method to convert Celsius to Fahrenheit
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    # Static method to convert Fahrenheit to Celsius
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    # Static method to convert Celsius to Kelvin
    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15
    
    # Static method to convert Kelvin to Celsius
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

# Example usage
if __name__ == "__main__":
    # Converting Celsius to Fahrenheit
    celsius = 25
    fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    
    # Converting Fahrenheit to Celsius
    fahrenheit = 98.6
    celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    
    # Converting Celsius to Kelvin
    celsius = 30
    kelvin = TemperatureConverter.celsius_to_kelvin(celsius)
    print(f"{celsius}°C is equal to {kelvin:.2f}K")
    
    # Converting Kelvin to Celsius
    kelvin = 300
    celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
    print(f"{kelvin}K is equal to {celsius:.2f}°C")
