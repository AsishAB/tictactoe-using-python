import random
from IPython.display import clear_output

myList=['','','','','','','','','',]
random_players=['X','O']
myListLength = len(myList)

#View List in a board
def displayList(list):
    clear_output()
    print(list[0] + " | " + list[1] + " | " +list[2] )
    print(list[3] + " | " + list[4] + " | " +list[5] )
    print(list[6] + " | " + list[7] + " | " +list[8] )
    
#Input choices for X or O
def userInputChoices():
    choice = 'True'
    while choice not in random_players:
        choice = input("Please Enter your choice (X, O):  ")
        
        if(choice not in random_players):
            print("This is an invalid choice. Please select one of the following options "+str(random_players))
            choice = 'wrong'
    return choice

#Input index choice
def userIndexChoices(playernumber):
    indexChoice = ''
    tempNumber = ''
    
    acceptable_range = range(1,10)
    visible_range = range(1,9)
    
    while indexChoice not in acceptable_range or indexChoice.isdigit() == True or indexChoice != 'wrongposition':
        tempChoice = input("Please enter an index between "+str(visible_range)+" for player "+str(playernumber)+" : ")
        
        if tempChoice.isdigit() == False:
            print("This is not an acceptable value. Please input an integer")
            indexChoice = 'wrong'
        else:
            tempNumber  = int(tempChoice)
            tempNumber = tempNumber
            #print(tempNumber)
            if tempNumber not in acceptable_range:
                print("The input value exceeds the acceptable range of "+str(visible_range))
                indexChoice = 'wrong'
            elif myList[tempNumber-1] != '':
                print("This position is taken. Please select a different choice")
                indexChoice = 'wrongposition'
            else:
                indexChoice = int(tempChoice)
                return indexChoice

            
#Toss Player for who goes first
def playerToss():
    random_option = random_players
    random.shuffle(random_option)
    #print(random_option)
    print("Player with "+random_option[0]+" will go first")
    return random_option


#Ask players if they want to continue
def continueGame():
    options  = True
    optionList1=['Yes', 'Y','y','yes','YES']
    optionList2=['No','no','n','NO','N']
    userChoice = ''
    while userChoice not in optionList1 and userChoice not in optionList2:
        userChoice = input("Want to continue the game ? (Y,N) :")
        if(userChoice not in optionList1 and userChoice not in optionList2):
            print("This is not the correct option. Please enter either Y or N.")
            userChoice = ''
            
    if(userChoice in optionList1):
        global myList
        myList=['','','','','','','','','',]
        options =  True
    else:
        options =  False
        
    
    return options


#Check if anyone has won
def check_winner(list):
    
        if((list[0] == 'X' and list[1] == 'X' and list[2] == 'X') or (list[3] == 'X' and list[4] == 'X' and list[5] == 'X') or (list[6] == 'X' and list[7] == 'X' and list[8] == 'X') 
          or (list[0] == 'X' and list[3] == 'X' and list[6] == 'X') or (list[1] == 'X' and list[4] == 'X' and list[7] == 'X') or (list[2] == 'X' and list[5] == 'X' and list[8] == 'X')
          or (list[0] == 'X' and list[4] == 'X' and list[8] == 'X') or (list[2] == 'X' and list[4] == 'X' and list[6] == 'X')):
            print("Player with 'X' has won")
            winner = True
        elif((list[0] == 'O' and list[1] == 'O' and list[2] == 'O') or (list[3] == 'O' and list[4] == 'O' and list[5] == 'O') or (list[6] == 'O' and list[7] == 'O' and list[8] == 'O') 
          or (list[0] == 'O' and list[3] == 'O' and list[6] == 'O') or (list[1] == 'O' and list[4] == 'O' and list[7] == 'O') or (list[2] == 'O' and list[5] == 'O' and list[8] == 'O')
          or (list[0] == 'O' and list[4] == 'O' and list[8] == 'O') or (list[2] == 'O' and list[4] == 'O' and list[6] == 'O')):
            print("Player with 'O' has won'")
            winner = True
        else:
            winner = False
            
        return winner
    

#main function that starts the game
def TicTacToeGame():
    
    
    continue_game = True
    winner = False
   
    while continue_game:
        #myList=['','','','','','','','','',]
        choice1 = userInputChoices()
        choice2=''
        if(choice1 == 'X'):
           choice2='O'
        else:
           choice2='X'  
        #print(choice2)    
        player = playerToss()
        player1 = player[0]
        player2 = player[1]
        i = 0
        while i < myListLength:
            #print(i)

            if(i%2==0):

                #print("Here")
                position1 = userIndexChoices(1)
                myList[position1-1] = player1
                #assignValues(position1-1 , player1)
                displayList(myList)
                winner = check_winner(myList)
                if(winner):
                    break

            elif(i%2!=0):
                #print("Not Here")
                position2 = userIndexChoices(2)
                #assignValues(position2-1 , player2)
                myList[position2-1] = player2
                displayList(myList)
                winner = check_winner(myList)
                if(winner):
                    break

            i += 1
            
        continue_game = continueGame()
            
        
       
    
TicTacToeGame()