import pywhatkit
from datetime import datetime

now = datetime.now()
hours = int(now.strftime("%H"))
type_hour = type(hours)
print(type_hour)
print("Current Time =", hours)
minutes = int(now.strftime("%M")) + 1
type_minutes = type(minutes)
print(type_minutes)
print("Current Time =", minutes)


pywhatkit.sendwhatmsg('+919022841846','Face found on Face detection',hours,minutes)