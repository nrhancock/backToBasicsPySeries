import random
import pymel.core as pm
import maya.mel as mel
import maya.cmds as cmds 

#count is set at 1
count = 0 
#a list on ints
list = (1,2,3,4)
#define parts of the list
even = (list[1],list[3])
odd = (list[0],list[2])
#lists of lists
numbers = [even, odd]
#random selection
def randSelect():
    global randomizer
    randomizer = random.choice(list)
    
def countUp():
    global count
    count += 1

def countDown():
    global count
    count -= 1
#function to add or subtract from the total in count 
def logicFunction():

    #in the event the randomizer is even will add 1
    if randomizer in even:
        countUp()
    #otherwise if it is odd it will subtract 1
    elif randomizer in odd:
        countDown()
#selects random item from list of numbers 

countSelections = 0
#runs the function
while count <=9:
    
    randSelect()
    #global countSelections
    #print(randomizer)
    logicFunction()
    countSelections += 1

print ('The count has reached: '+ str(count))
print ('This took ' + str(countSelections) + ' attempts')

if count >= 10:
    count = 0
    countSelection = 0
    print ("The counts have been reset")
    #print (count)
    #print (countSelection)
