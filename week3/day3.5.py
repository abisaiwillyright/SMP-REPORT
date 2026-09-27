# The datetime Module

from datetime import datetime, date

# Today's time and date
now = datetime.now()
print('Current datetime:', now)
print()

# Just the date
today = date.today()
print('Today:', today)
print('Year:', today.year)
print('Month:', today.month)
print('Today:', today.day)
print()

# Days between two dates
start = date(2025, 1, 1)
end = date(2025, 12,31)
delta = end - start
print('Days in 2025:', delta.days)
print()

# How many days until a goal date?
today = date.today()
goal_date = date(2025,12,31)
days_left = (goal_date - today). days

print(f' Days untill end  of 2025: {days_left}')
print()

# Format the date as text
formatted = today.strftime('%d %B %Y')
print('Today date:', formatted)