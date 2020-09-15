x = input('Enter first Number : ')
y = input('Enter Second Number : ')
z = input('Enter Third Number : ')
'''
if int(x) > int(y) :
    if int(x) > int(z):
        print(x + ' is larget number')
    else:
        print(z + ' is largest number')
else:
    if int(y) > int(z):
        print(y + ' is largest number')
    else:
        print(z + ' is largest number')
'''
# Alternate - by using operators :

if ((int(x) > int(y)) and (int(x) > int(z))):
    print(x + ' is largest number')
elif (int(y) > int(x)) and (int(y) > int(z)):
    print(y + ' is largest number')
else:
    print(z + ' is largest number')