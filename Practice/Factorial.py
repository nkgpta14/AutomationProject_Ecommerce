x = int(input('Enter a number : '))
fact = 1
def factorial():
    'This is factorial function'

    for i in range (1,x+1) :
        fact = fact * i
        #print(fact)
    print(fact)

factorial()