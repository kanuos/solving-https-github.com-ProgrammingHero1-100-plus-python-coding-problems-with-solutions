# Miles to Kilometers
# The Problem
# Convert miles to kilometers.

try:
    miles = float(input("Enter the length in miles : "))
    if miles < 0:
        print("Length cannot be negative")
    else:
        kilo_meter = miles * 1.60934
        print(f"{miles} miles = {kilo_meter} km")
except ValueError:
    print("Length must be a number")
