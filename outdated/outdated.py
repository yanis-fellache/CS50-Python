mth = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

coma = "no"

while True:
    try:
        date = input("Date: ").strip()
        try:
            month, day, year = date.split("/")
            coma = "no matter"

        except ValueError:
            month, day, year = date.split(" ")
            if month in mth:
                month = mth[month]
            if day[-1] == ",":
                coma = "yes"

            day = day.strip(",")


        if int(month) > 12:
            raise Exception
        else:
            pass
        if int(day) > 31:
            raise Exception
        else:
            pass
        if coma == "no":
            raise Exception
        else:
            pass


        break
    except:
        pass

if len(str(day)) < 2 :
    day = "0" + str(day)
if len(str(month)) < 2 :
    month = "0" + str(month)

print(year, month, day, sep="-")