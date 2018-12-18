def suffix(day):
    convert = str(day)
    if convert[-1:] == "1":
        return "st"
    elif convert[-1:] == "2":
        return "nd"
    elif convert[-1:] == "3":
        return "rd"
    else:
        return "th"


def formattedDate(day, month, year):

    months= ["","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if month == 0 or month > 12:
        print("This value is not valid")
    elif month == 2:
        if day <= 29:
            print(day,suffix(day),months[month], year)
        else:
            print("The month", months[month], "only has 1-29 days")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day <= 30:
            print(day,suffix(day),months[month], year)
        else:
            print("The month", months[month], "only has 1-30 days")
    else:
        print(day,suffix(day),months[month], year)

formattedDate(31,4,1997)
