#Rock, Paper, Scissors
#Back To Basic Py Series 
#by Nate Hancock

import pymel.core as pm
import maya.cmds as cmds 
import random

currentRound = 0
playersScore = 0
computersScore = 0
outcomes = ['Rock', 'Paper', 'Scissors']

def playerWindow():
    #every time player chooses the computer rerolls
    global computerOuput
    computerOuput = random.choice(outcomes)
    
    #player input 
    global playerPrompt
    playerPrompt = cmds.promptDialog(
                title='Rock, Paper, Scissors',
                message='Enter your selection: ',
                button=['OK', 'Repeat Choice'],
                defaultButton='OK',
                cancelButton='Repeat Choice',
                dismissString='Repeat Choice')
                
    if playerPrompt == 'OK':
        global playerChoice
        playerChoice = str(cmds.promptDialog(query=True, text=True))

#runs the game
def startGame():
    playerWindow()

    if playerChoice not in outcomes:
        print ('Please type Rock, Paper, or Scissors')
        print ('You selected: ' + playerChoice)

    elif playerChoice in outcomes:
        print ('You choose: ' + playerChoice)
        finalResult()

#the win funtion
def playerWins():
    global currentRound
    global playersScore
    print ('You Win!')
    print ('------------')
    currentRound += 1
    playersScore += 1
    print ('------------')
    print ('------------')
    print ('Current round: ' + str(currentRound))
    print ('Players score is: ' + str(playersScore))
    print ('Computers score is: ' + str(computersScore))
    print ('------------')
    

#the lose funstion
def playerLoses():
    global currentRound
    global computersScore
    print ('Sorry, you lose.')
    print ('------------')
    computersScore += 1 
    currentRound += 1
    print ('------------')
    print ('Current round: ' + str(currentRound))
    print ('------------')
    print ('------------')
    print ('Players score is: ' + str(playersScore))
    print ('Computers score is: ' + str(computersScore))
    print ('------------')

#the tie function
def playerTie():
    global currentRound
    print ('------------')
    print ('Its a tie, try again.')
    print ('------------')
    print ('Current round: ' + str(currentRound))
    print ('------------')
    print ('------------')
    print ('Players score is: ' + str(playersScore))
    print ('Computers score is: ' + str(computersScore))
    print ('------------')

#determines the winner
def finalResult():
    print ('You have selected: ' + playerChoice)
    print ('Your opponent has selected: ' + computerOuput)
    
    #have to be global so they can be referenced and modified 

    if playerChoice == computerOuput:
        
        playerTie()
    
    elif (playerChoice == outcomes[0] and computerOuput == outcomes[2]) or (playerChoice == outcomes[1] and computerOuput == outcomes[0]) or (playerChoice == outcomes[2] and computerOuput == outcomes[1]):
        
        playerWins()
        
    elif (playerChoice == outcomes[0] and computerOuput[1]) or (playerChoice == outcomes[1] and computerOuput[2]) or (playerChoice == outcomes[2] and computerOuput[0]):
        
        playerLoses()

while currentRound <= 4:
        startGame()

if currentRound >= 5 and playersScore >= computersScore:
    print ('------------')
    print ('You won the game, congratulations')
    print ('------------')
    
    currentRound = 0
    playersScore = 0
    computersScore = 0
    
elif currentRound >= 5 and playersScore <= computersScore:
    print ('------------')
    print ('You lost the game. :(')
    print ('------------')
    
    currentRound = 0
    playersScore = 0
    computersScore = 0
    
