from datetime import datetime, timedelta

from convertdate import hebrew


def create_dates(date, num, step):
    # get the start date from the str, then map n numbers to the start + n*step
    start_date = datetime.strptime(date, "%Y-%m-%d")
    return list(map(lambda d: (start_date + timedelta(days=d * step)).strftime("%Y-%m-%d"), list(range(num))))


def create_hebrew_dates(date, num, step):
    # at first get the normal date (gregorian) with the convertdate.hebrew library
    year, month, day = map(int, date.split("-"))
    g_year, g_month, g_day = hebrew.to_gregorian(year, month, day)
    gregorian_str = f"{g_year:04d}-{g_month:02d}-{g_day:02d}"

    # then we used the first function that create the list of dates - than convert back to hebrew all the list
    return list(map(lambda d: hebrew.from_gregorian(int(d.split("-")[0]), int(d.split("-")[1]), int(d.split("-")[2])),
                    create_dates(gregorian_str, num, step)))


print(create_hebrew_dates("5770-12-12", 50, 2))
