# Take a birthday of a person and then calculate the age.
import datetime


def days_to_month(d):
    y = d // 365
    d %= 365
    m = d // 30
    d %= 30
    return f"{y} years, {m} months and {d} days "


try:
    year = int(input("Enter your birth year : "))
    month = int(input("Enter your birth month in number : "))
    day = int(input("Enter your birth date : "))
    d_o_b = datetime.date.fromisoformat(f"{year}-{month if month > 9 else f'0{month}'}-{day}")
    today = datetime.date.today()
    days = (today - d_o_b).days
    print(f"You are {days_to_month(days)} old.")

except ValueError as err:
    print(err)
