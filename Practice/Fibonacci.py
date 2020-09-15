x = int(input('Enter a number : '))
j = 0
k = 1
#l = ''

#print(j,',',k, end = '')
#print(k, end = '')
while j < x:
#for i in range (3,x+1) :
    #l = j + k
    print(j, end = '')
    j = k
    k = j + k
    #print(',',l,end='')
'''

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

fib(10)'''