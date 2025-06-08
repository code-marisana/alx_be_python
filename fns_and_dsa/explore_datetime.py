from datetime import date
import datetime
def display_current_datetime():
    current_date = datetime.datetime.today()
    print(f"Current date and time: {current_date.year}-{current_date.strftime("%m")}-{current_date.strftime("%d")} {current_date.strftime("%H")}:{current_date.strftime("%M")}:{current_date.strftime("%S")}")

display_current_datetime()