def sum(a , b):                         #def function_name(parameters):        (Don't forget the colon at the end)
    print(a + b)

a = 4
b = 12
sum(a , b)

def multiply(a , b = 6):                #passed a default value to b... if no value is passed it will take 6 by default
    print(a * b)

a = 5
multiply(a)                             #no value for b is passed
