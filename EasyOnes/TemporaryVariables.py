# Swap two variables
# The problem
# Swap two variables.
#
# To swap two variables: the value of the first variable will become the value of the second variable.
# On the other hand, the value of the second variable will become the value of the first variable.
#
# Hints
# To swap two variables, you can use a temp variable.

var1 = input("Enter variable 1 : ")
var2 = input("Enter variable 2 : ")
# without using temporary variables
print(f"Before swapping : A = {var1}, B = {var2}")
var1, var2 = var2, var1
print(f"After swapping <py way> : A = {var1}, B = {var2}")
var1, var2 = var2, var1
print(f"Before swapping : A = {var1}, B = {var2}")
temp = var1
var1 = var2
var2 = temp
print(f"After swapping <temp variable> : A = {var1}, B = {var2}")
