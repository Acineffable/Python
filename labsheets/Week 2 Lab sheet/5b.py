from datetime import datetime
hour = input("Hours:")
minute = input("Minutes:")
h = datetime.strptime(hour, "%H")
m = datetime.strptime(minute, "%M")
h12 = h.strftime("%I")
m12 = m.strftime("%M")

if int(minute) < 5:
    if int(hour)>12:
        print(h12,"00","PM")
    else:
        print(h12,"00","AM")

if int(minute) >= 5 and int(minute) < 15:
    if int(hour)>12:
        print(h12,15,"PM")
    else:
        print(h12,15,"AM")

if int(minute) >= 15 and int(minute) < 20:
    if int(hour)>12:
        print(h12,20,"PM")
    else:
        print(h12,20,"AM")
        
if int(minute) >= 20 and int(minute) < 25:
    if int(hour)>12:
        print(h12,25,"PM")
    else:
        print(h12,25,"AM")
        
if int(minute) >= 25 and int(minute) < 30:
    if int(hour)>12:
        print(h12,30,"PM")
    else:
        print(h12,30,"AM")

if int(minute) >= 30 and int(minute) < 35 :
    if int(hour)>12:
        print(h12,35,"PM")
    else:
        print(h12,35,"AM")

if int(minute) >= 40 and int(minute) < 45 :
    if int(hour)>12:
        print(h12,45,"PM")
    else:
        print(h12,45,"AM")

if int(minute) >= 45 and int(minute) < 50 :
    if int(hour)>12:
        print(h12,55,"PM")
    else:
        print(h12,55,"AM")

if int(minute) >= 50 and int(minute) < 55 :
    if int(hour)>12:
        print(h12,00,"PM")
    else:
        print(h12,00,"AM")

