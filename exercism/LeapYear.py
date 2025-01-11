def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
                print('true')
            else:
                print('False')
                return False
        else:
            print('true')
            return True
    else:
        print('False')
        return False

leap_year(1992)