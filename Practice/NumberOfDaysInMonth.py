month = input('Enter Month : ')
try:
    if ((('JAN' in month.upper()) or ('MAR' in month.upper()) or ('MAY' in month.upper()) or ('JUL' in month.upper()) or ('AUG' in month.upper()) or ('OCT' in month.upper()) or ('DEC' in month.upper()))
                        or (int(month) == 1) or (int(month) == 3) or (int(month) == 5 )or (int(month) == 7) or (int(month) == 8 )or (int(month) == 10) or (int(month) == 12)):
        print('Number of days in ' + month + ' is 31')

    elif ((('APR' in month.upper()) or ('JUN' in month.upper()) or ('SEP' in month.upper()) or ('NOV' in month.upper()))
                        or (int(month) == 4) or (int(month) == 6) or (int(month) == 5) or (int(month) == 9) or (int(month) == 11)):
        print('Number of days in ' + month + ' is 30')

    elif ((('FEB' in month.upper()) or int(month) == 2)):
        print('Number of days in ' + month + ' is 28')
    else:
        print('not a valid month')
except:
    print('Not a valid Month')