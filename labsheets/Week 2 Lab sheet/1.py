from datetime import datetime
userTime = input("What time is it?")
d = datetime.strptime(userTime, "%H.%M")
time = d.strftime("%I.%M")
convert = float(userTime)
if convert>12.00:
    print(time, "PM")
else:
    print(time, "AM")
