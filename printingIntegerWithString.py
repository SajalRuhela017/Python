val = input("Enter the denomintion of the currency you have: ")
num = input("Enter the total number of currency notes you have: ")
ans = int(num) * int(val)
print("Your " + str(num) + " notes of value " + str(val) + " each equals " + str(ans) + ".")