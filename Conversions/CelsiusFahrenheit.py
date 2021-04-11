# Celsius to Fahrenheit
# The problem
# Take the temperature in degrees Celsius and convert it to Fahrenheit.

try:
    celsius = float(input("Enter the temperature in Celsius : "))
    fahrenheit = ((celsius * 9) + 160) / 5
    print(f"{celsius} °C = {fahrenheit} °F")
except ValueError:
    print("Temperature input must be a number")
