# Compound Interest
# Compound interest formula is:
# A = P(1+r/100)t
# Here, P is the principal amount; it is the amount that you borrowed.
# r is the interest rate in percentage and t is the time.

try:
    p = float(input("Enter the principal amount : "))
    r = float(input("Enter the rate of interest(%) : "))
    r /= 100
    f = 2
    print("""Compounding frequency : 
    Press 1 for monthly
    Press 2 for bi-monthly
    Press 4 for quarterly
    Press 6 for half-yearly""")
    temp = int(input("Enter the compounding frequency : "))
    if temp in [1, 2, 4, 6]:
        f = temp
    t = float(input("Enter the time period : "))
    a = p * (1 + r / f) ** (f * t)
    print(f"Compounded amount : {round(a, 2)}")
    print(f"Compounded interest : {round(a - p, 2)}")
    si = p * t * r
    a = p + si
    print(f"Simple Interested amount : {round(a, 2)}")
    print(f"Simple interest : {round(si, 2)}")
except ValueError:
    print("Inputs must be numbers")
