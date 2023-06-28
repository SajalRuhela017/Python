from tkinter import *
import random

def nextTurn(row, column):
    
    global player
    if buttons[row][column]['text'] == "" and checkWinner() is False:
        buttons[row][column]['text'] = player

        if player == players[0]:

            if checkWinner() is False:
                player = players[1]
                label.config(text = (players[1] + "'s turn"))
            elif checkWinner() is True:
                label.config(text = (players[0] + " Wins"))
            elif checkWinner() == "Tie":
                label.config(text = ("Tie!"))
        else:

            if checkWinner() is False:
                player = players[0]
                label.config(text = (players[0] + "'s turn"))
            elif checkWinner() is True:
                label.config(text = (players[1] + " Wins"))
            elif checkWinner() == "Tie":
                label.config(text = ("Tie!"))

def checkWinner():
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg = "green")
            buttons[row][1].config(bg = "green")
            buttons[row][2].config(bg = "green")
            return True
        
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            buttons[0][col].config(bg = "green")
            buttons[1][col].config(bg = "green")
            buttons[2][col].config(bg = "green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg = "green")
        buttons[1][1].config(bg = "green")
        buttons[2][2].config(bg = "green")
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg = "green")
        buttons[1][1].config(bg = "green")
        buttons[2][0].config(bg = "green")
        return True

    elif emptySpaces() is False:
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg = "yellow")
        return "Tie"

    else:
        return False

def emptySpaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] != "":
                spaces -= 1
    
    if spaces == 0:
        return False
    else:
        return True

def newGame():
    global player

    player = players[0]
    label.config(text = player + "'s turn")

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text = "", bg = "lightblue")



######### Main Body #########

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [ [0,0,0], 
            [0,0,0], 
            [0,0,0] ]
label = Label(text = player + "'s turn", font = ('consolas', 40))
label.pack(side = "top")

reset_button = Button(text = "restart", font = ('consolas', 20), command = newGame)
reset_button.pack(side = "top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text = "", font = ('consolas', 40), width = 5, height = 2, 
                                   command = lambda row = row, column = col: nextTurn(row, column))
        buttons[row][col].grid(row = row, column = col)
        buttons[row][col].config(bg="lightblue")

window.mainloop()