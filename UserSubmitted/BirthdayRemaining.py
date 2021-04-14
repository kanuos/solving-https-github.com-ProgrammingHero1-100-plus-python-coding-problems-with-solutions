# Birthday remaining
# The problem
# Calculate how many days are remaining for the next birthday.
import datetime


def countdown_to_b_day(d):
    y = d // 365
    d %= 365
    m = d // 30
    d %= 30
    return y + 1, f"{12 - m} months and {d} days "


try:
    year = int(input("Enter your birth year : "))
    month = int(input("Enter your birth month in number : "))
    day = int(input("Enter your birth date : "))
    d_o_b = datetime.date.fromisoformat(f"{year}-{month if month > 9 else f'0{month}'}-{day}")
    today = datetime.date.today()
    days = (today - d_o_b).days
    next_year, countdown = countdown_to_b_day(days)
    print(f"Your {next_year}th birthday is in {countdown}.")

except ValueError as err:
    print(err)
