students = ["Ram", "Laxman" , "Bharat" , "Shatrughan" , "Hanuman"]

#break statement

for i in students:
    if i == "Shatrughan":
        break
    print(i)

print()
#continue statement

for i in students:
    if i == "Bharat":
        continue
    print(i)
