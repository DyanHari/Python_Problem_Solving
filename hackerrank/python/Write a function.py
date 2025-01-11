def is_leap(year):
    leap = False

    if year % 4 == 0:  # If the year is evenly divisible by 4, check the next condition
        if year % 100 == 0:  # If the year is evenly divisible by 100, check the next condition
            if year % 400 == 0:  # If the year is evenly divisible by 400, it's a leap year
                leap = True
        else:  # If the year is evenly divisible by 4 but not by 100, it's a leap year
            leap = True
    return leap  # If the year is divisible by 4 and 100 but not by 400, it's not a leap year


year = int(input())
