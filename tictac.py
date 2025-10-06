from colorama import Fore, Style, init
import random
from math import inf
init(autoreset=True)


def getSymbol(sym):
    if sym == "x":
        return Fore.RED + "X" + Style.RESET_ALL
    elif sym == "o":
        return Fore.BLUE + "O" + Style.RESET_ALL
    return " "



def printBoard():
    
    print("", getSymbol(board[0]), "|", getSymbol(board[1]), "|", getSymbol(board[2]))
    print("---|---|---")
    print("", getSymbol(board[3]), "|", getSymbol(board[4]), "|", getSymbol(board[5]))
    print("---|---|---")
    print("", getSymbol(board[6]), "|", getSymbol(board[7]), "|", getSymbol(board[8]))


def checkWinner():
    global x
    for i in range(0,7,3):
        if board[i] != " " and board[i]==board[i+1]==board[i+2]:
            print("Player",board[i],"Won")
            
            return True
    for i in range(3):
        if board[i] != " " and board[i]==board[i+3]==board[i+6]:
            print("Player",board[0],"Won")
            
            return True
    if board[0]!= " " and board[0]==board[4]==board[8]:
        print("Player",board[0],"Won")
        
        return True
        
    elif board[2] != " " and board[2]==board[4]==board[6]:
        print("Player",board[2],"Won")
        
        return True
    if board.count(" ") == 0:
        print("Draw")
        x-=1
        return True
    return False
    
def doAgain():
    global running,board,mode
    choice = input("Do you wanna continue (y/n): ")
    if choice.lower() == 'y':
        running = True
        board = [" "]*9
        mode = int(input("Enter which mode you wanna play mode:1 computer, mode:2 2 player (1/2): "))

        printBoard()
    else:
        running = False    

def makeMove(xox):
    while True:
        try:
            move = int(input(f"Type where you want to place your {xox} : "))
            if move <0 or move >8:
                print("please enter a valid index of the box")
                continue
            if board[move] != " ":
                print("The column is already taken")
                continue
            board[move] = xox
            break
        except ValueError:
            print("Enter a valid number between 0 to 8")
            
        
def printScore():
    if mode == 2:
        print("Scoreboard")
        print("Player 1 (X) | Player 2 (O)")
        print("-------------|-------------")
        print("      ",x,"    |      ",o,"")          
    else:
        print("Scoreboard")
        print("Player 1 (X) | Computer (O)")
        print("-------------|-------------")
        print("      ",x,"    |      ",c,"") 
        
def computerMove():
    emptyCell = [i for i,v in enumerate (board) if v == " " ]
    move = random.choice(emptyCell)
    board[move] = "o"  
    
def whoWin(xo):
    for i in range(0,7,3):
        if board[i] == xo and board[i]==board[i+1]==board[i+2]:
            return True
    for i in range(3):
        if board[i] == xo and board[i]==board[i+3]==board[i+6]:
            return True
    if board[0]== xo and board[0]==board[4]==board[8]:
        return True
    elif board[2] == xo and board[2]==board[4]==board[6]:
        return True
    
        
def minMax(board,isMaximizing,depth=0):
    
    if whoWin("x"):
        
        return -1
    elif whoWin("o"):
        
        return 1
    elif " " not in board:        
        return 0
    else:
        if isMaximizing:
            bestScore = -inf
            move = None
            for i,v in enumerate(board):
                if v == " ":
                    board[i] = "o"
                    currentScore = minMax(board,False, depth + 1)
                    board[i] = " "
                    if currentScore > bestScore:
                        bestScore = currentScore
                        move = i
            if depth ==0 and move is not None:
                board[move] = "o"
            return bestScore
        else:
            bestScore = inf
            for i,v in enumerate(board):
                if v == " ":
                    board[i] = "x"
                    currentScore = minMax(board,True,depth + 1)
                    board[i] = " "
                    if currentScore < bestScore:
                        bestScore = currentScore
            return bestScore

                
        
        
    
x = 0
o = 0
c = 0
board = [" "]*9
printBoard()
running = True

while True:
    try:
        mode = int(input("Enter which mode you wanna play mode:1 computer, mode:2 2 player (1/2): "))
        if mode !=1 and mode !=2:
            print("Enter 1 or 2")
            continue
        else:
            break
    except ValueError:
            print("Please Enter 1 or 2")
    
    
while  running:
    if checkWinner():
        break
    print("Player one's turn: put 'x'")
    makeMove('x')
    printBoard()
    
    if checkWinner():
        x+=1
        printScore()
        doAgain()
        continue
    
    if mode == 2:
        print("Player two's turn: put 'o' ")
        makeMove('o')
        printBoard()
        if checkWinner():
            o+=1
            printScore()
            doAgain()
            continue
    else:
        print("\n")
        print("Computer Move\n\n")
        minMax(board,isMaximizing=True)
        
        printBoard()
        if checkWinner():
            c+=1
            printScore()
            doAgain()
            continue
