month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']


def problem19():
    matches = []
    offset = 1
    for year in range(0, 101):
        if year > 0 and year % 4 == 0:
            md = month_days_leap
        else:
            md = month_days
        for m in range(0, 12):
            if m == 6 and year == 0:
                print(f"{months[m]} :: {md[:m]} :: {sum(md[:m])} :: {sum(md[:m]) + offset} :: {(sum(md[:m]) + offset) % 7}")
            if (sum(md[:m]) + offset) % 7 == 0 and year > 0:
                matches.append((1900 + year, months[m]))
        offset = (sum(md) + offset) % 7
    for match in matches:
        print(f"match: {match}")
    print(f"Problem 19 answer: {len(matches)}")


# if year starts on a monday, then begin_offset = 6
# for each month, sum of first_of_year_offset + sum(month_dayx[0:month_index]) = offset for next first-of-month

# mon, jan 1, 1900 (not leap, first_of_year_offset = 6)
# sun, jan 7, 14, 21, 28, 1900 (first sundays)
# thu, feb 1, 1900 (first of second month)
# thu, mar 1, 1900 (first of third month)
# sun, apr 1, 1900 (first of fourth month)
# (31 - 6) % 7 = 4  # (count_month_days - year_offset) % days_in_week


problem19()
