# Simple Interest
# The Problem
# You borrowed $5000 for 2 years with 2% interest per year.
# Calculate the simple interest to know how much you have to pay?

try:
    principal = float(input("Enter the principal : "))
    rate_of_interest = float(input("Enter the rate of interest : "))
    period = float(input("Enter the period : "))
    si = principal * rate_of_interest * period / 100
    print(f"The simple interest : {si}")
except ValueError:
    print("Inputs must be numbers")
