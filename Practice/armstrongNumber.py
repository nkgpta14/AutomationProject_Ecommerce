x = int(input('Enter a number : '))
sum = 0
y = x
while y>0:
    digit = y%10
    sum += digit**3
    y //= 10
if sum == x:
    print('armstrong number')
else:
    print('not armstrong number')
