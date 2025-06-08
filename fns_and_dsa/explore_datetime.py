from datetime import date
import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.year}-{current_date.strftime("%m")}-{current_date.strftime("%d")} {current_date.strftime("%H")}:{current_date.strftime("%M")}:{current_date.strftime("%S")}")

display_current_datetime()

def calculate_future_date():
    future_date = datetime.datetime.now() + datetime.timedelta(days=int(input("Enter the number of days to add to the current date: ")))
    print(f"Future date: {future_date.year}-{future_date.strftime("%m")}-{future_date.strftime("%d")}")

calculate_future_date()