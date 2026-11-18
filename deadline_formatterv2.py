from datetime import date

event_title = input("Enter event title: ").strip()
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_date = date(year, month, day)
formatted_title = event_title.upper()
month_name = event_date.strftime("%B")
weekday_name = event_date.strftime("%A")
readable_date = f"{month_name} {event_date.day}, {event_date.year}"

print("\nFormatted Output:")
print(f"Event: {formatted_title}")
print(f"Date: {readable_date}")
print(f"Year: {event_date.year}")
print(f"Month: {month_name}")
print(f"Day: {event_date.day}")
print(f"Weekday: {weekday_name}")