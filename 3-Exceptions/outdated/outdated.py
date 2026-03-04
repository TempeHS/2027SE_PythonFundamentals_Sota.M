month_dict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


import re

while True:
    date = input("Input date: ")

    if "/" in date:
        d1, d2, d3 = date.split("/")
        if int(d1) > 12 or int(d2) > 31:
            continue
        print(f"{d3}-{int(d1):02}-{int(d2):02}")
        break
    elif "," in date:
        d1, d2, d3 = re.split(r"[ ,]+", date)
        m = month_dict[d1]
        if m > 12 or int(d2) > 31:
            continue
        print(f"{d3}-{m:02}-{int(d2):02}")
        break
