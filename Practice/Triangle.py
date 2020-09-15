a = input('First side of the Triangle : ')
b = input('Second side of the Triangle : ')
c = input('Third side of the Triangle : ')

if a == b and b == c:
    print('Equilateral Triangle')
#elif ((a == b and b != c) or (a != b and b == c)):
elif a == b or b == c:
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')