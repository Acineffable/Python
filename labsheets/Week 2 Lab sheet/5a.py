from datetime import datetime
hour = input("Hours:")
minute = input("Minutes:")
h = datetime.strptime(hour, "%H")
m = datetime.strptime(minute, "%M")
h12 = h.strftime("%I")
m12 = m.strftime("%M")
if int(hour)>12:
    print(h12,m12,"PM")
else:
    print(h12,m12,"AM")



