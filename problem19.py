'''You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import time

start_time = time.time()

# mon 0, tue 1, wed 2, thu 3, fri 4, sat 5, sun 6
week_day = 0 # 1 jan 1900
day = 1
month = 1
year = 1901

counter = 0
while day != 1 or month != 1 or year != 2001:
    # print(day,"/", month,"/", year)
    if week_day == 6 and day == 1:
        counter += 1

    if week_day == 6:
        week_day = 0
    else:
        week_day += 1

    if month == 4 or month == 6 or month == 9 or month == 11:
        if day == 30:
            day = 1
            month += 1
        else:
            day += 1

    elif month == 12:
        if day == 31:
            day = 1
            month = 1
            year += 1
        else:
            day += 1

    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
        if day == 31:
            day = 1
            month += 1
        else:
            day += 1

    elif month == 2:
        # if leap year
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    if day == 29:
                        day = 1
                        month += 1
                    else:
                        day += 1
                else:
                    if day == 28:
                        day = 1
                        month += 1
                    else:
                        day += 1
            else:
                if day == 29:
                    day = 1
                    month += 1
                else:
                    day += 1
        else:
            if day == 28:
                day = 1
                month += 1
            else:
                day += 1
        # else

print(counter)

print("--- %s seconds ---" % (time.time() - start_time))

