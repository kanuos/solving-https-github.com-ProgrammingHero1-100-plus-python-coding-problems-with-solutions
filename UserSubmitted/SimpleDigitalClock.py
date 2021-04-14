# Simple Digital Clock
import time


def month_in_words(index):
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]
    return months[index]


def get_date_string():
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    day_suffix = "th"
    day = time.localtime().tm_mday
    if day % 10 == 1:
        day_suffix = "st"
    elif day % 10 == 2:
        day_suffix = "nd"
    elif day % 10 == 3:
        day_suffix = "rd"

    return f"{day}-{day_suffix} {month_in_words(month)}, {year}"


def get_current_time():
    hour = time.localtime().tm_hour
    mins = time.localtime().tm_min
    secs = time.localtime().tm_sec
    am_pm = "AM" if 12 > hour >= 0 else "PM"
    hour = hour - 12 if hour > 12 else hour

    return f"{hour} : {mins} : {secs} {am_pm}"


try:
    print(f"Today is {get_date_string()}")
    while True:
        print(get_current_time())
        time.sleep(1)
        keep_running = input("Press 'q' to stop clock..")
        if keep_running in ['q', 'Q']:
            print("Exiting gracefully...")
            break

except ValueError as err:
    print(err)
