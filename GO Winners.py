#Welcome to the Code Revolution
#This is a demo of two of the winners of our Grand Opening week giveaway
#Lessons in Python will follow this format (all code, all the time)
#In this lesson we will create a Dictionary of Customers that dropped by
#and then randomly choose two numbers from that Dictionary

#to use random functions in python we import that library
import random

#First create the lists to track the attendees and eventually the two winners
grandOpeningPeeps = []
grandOpeningWinners = []

#Then populate the list with a number value (key) and first name + last initial
grandOpeningPeeps.append("ms8384")
grandOpeningPeeps.append("sb1557")
grandOpeningPeeps.append("dr0650")
grandOpeningPeeps.append("kfs1045")
grandOpeningPeeps.append("lb4743")
grandOpeningPeeps.append("sb0634")
grandOpeningPeeps.append("ts7772")
grandOpeningPeeps.append("ad6100")
grandOpeningPeeps.append("tg6011")
grandOpeningPeeps.append("tb3522")

#pick the first winner and move them to the Winners list
firstWinner = random.choice(grandOpeningPeeps)
grandOpeningWinners.append(firstWinner)
#now remove them from the attendees so they can't win again
grandOpeningPeeps.remove(firstWinner)

#choose 2nd winnner and do the same, then remove them :)
secondWinner = random.choice(grandOpeningPeeps)
grandOpeningWinners.append(secondWinner)
#removing from attendees
grandOpeningPeeps.remove(secondWinner)

#choose 3rd winner, etc etc
thirdWinner = random.choice(grandOpeningPeeps)
grandOpeningWinners.append(thirdWinner)
#remove them
grandOpeningPeeps.remove(thirdWinner)
print("The Grand Opening Winners are:")
winnerNo = 1
for winner in grandOpeningWinners:
    print(str(winnerNo) + ": " + winner)
    winnerNo += 1

