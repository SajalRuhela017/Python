#Program to decide the winner in a cricket match

aus = input("Enter the score made by Australia: ")
ind = input("Enter the score made by India: ")
if(ind > aus):
    print("India won the match!!")
elif(aus > ind):
    print("Australia won the match!!")
else:
    print("The match ended in a tie!!")