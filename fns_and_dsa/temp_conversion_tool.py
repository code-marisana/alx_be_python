FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32

def temperature():
    user_temperature = input("Enter the temperature to convert: ")

    while not user_temperature.isnumeric():
        print("Invalid temperature. Please enter a numeric value.")
        user_temperature = input("Enter the temperature to convert: ")
    
    return float(user_temperature)

def convert_temperature():
    temp = temperature()
    match input("Is this temperature in Celsius or Fahrenheit? (C/F): "):
        case "C":
            print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
        case "F":
            print(f"{temp}°F is {convert_to_celsius(temp)}°C")


convert_temperature()