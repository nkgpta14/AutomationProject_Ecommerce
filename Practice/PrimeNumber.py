'''
x = int(input('Enter a number : '))

z=0
for i in range (2,x):
    if(x%i==0):
        print("Its not a Prime number")
        break
if(z==0):
    print("This is Prime number")
'''

for number in range (1,100) :
    for i in range(2, number):
        #print(i)
        if (number % i == 0):
            break
    else:
        print(number)