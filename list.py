marks = [93, 98, 91, 100]
print(marks)                #print all the elements
print(marks[0])             #prints 93
print(marks[-1])            #start printing in reverse order... prints 100
print(marks[0:3])           #prints elements from index 0 to 2

#printing list using for loop

for score in marks:
    print(score)

#functions on lists
marks.append(95)            #add the value st the the end of the list
for score in marks:
    print(score)

marks.insert(1, 96)         #insert the value at the given index
for score in marks:
    print(score)

print(97 in marks)              #will try to find the given value in list

print(len(marks))               #will print the length of the list

marks.clear()                   #will clear the list
print(marks)            