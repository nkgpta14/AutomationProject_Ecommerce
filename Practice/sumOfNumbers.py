
class A:

    def addNumbers(self,*args):
        sum = 0
        for numbers in args:
            sum = sum + numbers
        return sum


    #print(x)

    def multiplication(self,*args):
        product = 1
        for numbers in args:
            product = product * numbers
        return product

obj = A()
x = obj.addNumbers(10,20,30,40,50,60,70,80,90)
y = obj.multiplication(x,2,3,10)
print(y)

# Study about *args