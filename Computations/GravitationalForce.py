# Compute gravitational force between two objects.
# The formula for gravitational force is
# F = G m^1m^2/r^2
#
# Here G is the gravitational constant. Its value is 6.673*10-11
#
# So, take three input from the users.
# The mass of the first object, the mass of the second object and the distance between them.

try:
    print("Calculate Gravitational Force between two masses")
    m1 = float(input("Enter the mass of first body : "))
    m2 = float(input("Enter the mass of second body : "))
    r = float(input("Enter the distance between the two bodies : "))
    constant_g = 6.673 * 10 ** -11
    f = constant_g * m1 * m2 / r ** 2
    print(f"Force : {f}")

except ValueError:
    print("Inputs must be numbers")
