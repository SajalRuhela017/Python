a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
op = input("Enter the operation you want to perform: ")
if(op == '+'):
    print(int(a) + int(b))
elif(op == '-'):
    print(int(a) - int(b))
elif(op == '*'):
    print(int(a) * int(b))
elif(op == '/'):
    print(int(a) / int(b))
else:
    print(int(a) % int(b))