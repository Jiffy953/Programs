import random
x = 0 #player start x
y = 0 #player start y
treasureX = random.randint(-2, 2) #treasure x
treasureY = random.randint(-2, 2) #treasure y
obstacleOneX = random.randint(-2, 2) # obstacle
obstacleOneY = random.randint(-2, 2) # ""
obstacleTwoX = random.randint(-2, 2) #""
obstacleTwoY = random.randint(-2, 2) #""
obstacleThreeX = random.randint(-2, 2) #""
obstacleThreeY = random.randint(-2, 2) #""

# 
playerName = str(raw_input("Player, what is your name?: "))

print "Welcome to the game, " + playerName + ". You are given 20 turns to explore a 5x5 grid map. You will start on coordinate (0,0) with the maximum value of x and y being 2 and the minimum value being -2. If you attempt to pass these boundaries, a turn will be counted against you and you will stay in your current place. If you input a direction that is not specified for use, you will not move and a turn will be used. There are different obstacles you may encounter. You will have 2 attempts to get past your obstacle, otherwise the game will end. It is possible that you will run into 2 obstacles on the same grid, giving you the ability to get the past the second obstacle if you fail the first, this is a very rare occasion. The end goal is to find the treasure. Good luck, " + playerName + "!"
print "=======================================" #rules of the game
print "======================================="
turns = 0 #start number of turns 
bMove = True #the game runs when true


while bMove == True:
    
    move = str(raw_input("Which direction would you like to move, "+ playerName + "?(Up, Down, Left, Right(Check your spelling carefully!)): "))
    #line 27-46 is movement of up down left right either adding or subtracting to x or y, informing the user which direction they moved
    if move == "Up" or move == "up":
        print " "
        print str(playerName) + " moved up one grid square."
        print " "
        y = y + 1
    elif move == "Down" or move == "down":
        print " "
        print str(playerName) + " moved down one grid square."
        print " "
        y = y - 1
    elif move == "Left" or move == "left":
        print " "
        print str(playerName) + " moved left one grid square."
        print " "
        x = x - 1
    elif move == "Right" or move == "right":
        print " "
        print str(playerName) + " moved right one grid square."
        print " "
        x = x + 1
    #line 48-71 classifies the barriers of the map, reverts the player back if they try to pass a barrier and informs them which directions they are able to move    
    if x == 3:
        x = 2
        print "===================="
        print " "
        print "*You have hit the barrier. Move up, down or left.*"
        print " "
    elif x == -3:
        x = -2
        print "===================="
        print " "
        print "*You have hit the barrier. Move up, down or right.*"
        print " "
    elif y == 3:
        y = 2
        print "===================="
        print " "
        print "*You have hit the barrier. Move down, left or right.*"
        print " "
    elif y == -3:
        y = -2
        print "===================="
        print " "
        print "*You have hit the barrier. Move up, left or right.*"
        print " "
    #obstacle 1 uses a while loop with a counter of 2 to get the correct answer or the game ends
    if x == obstacleOneX and y == obstacleOneY:
        obstacleOne = True
        attemptsOne = 0
        print " "
        print "You have hit an obstacle! Answer the following question correctly to pass."
        print " "
        while obstacleOne == True:
            answerOne = str(raw_input("What is 56 + 34?(in numeric form): "))
            if answerOne == "90":
                print " "
                print "Correct, you shall pass."
                print " "
                obstacleOne = False
            elif answerOne != "90":
                print " "
                print "That was incorrect! You have one more attempt to get it correct or goodbye. "
                print " "
                attemptsOne = attemptsOne + 1
            if attemptsOne == 2:
                    obstacleOne = False
                    bMove = False
    #obstacle 2 uses a while loop with a counter of 2 to get the correct answer or the game ends                
    if x == obstacleTwoX and y == obstacleTwoY:
        obstacleTwo = True
        attemptsTwo = 0
        print " "
        print "You have hit an obstacle! Answer the following question correctly to pass."
        print " "
        while obstacleTwo == True:
            answerTwo = str(raw_input("What is 75 divided by 5?(in numeric form): "))
            if answerTwo == "15":
                print " "
                print "Correct, you shall pass."
                print " "
                obstacleTwo = False
            elif answerTwo != "15":
                print " "
                print "That was incorrect! You have one more attempt to get it correct or goodbye. "
                print " "
                attemptsTwo = attemptsTwo + 1
            if attemptsTwo == 2:
                    obstacleTwo = False
                    bMove = False
    #obstacle 3 uses a while loop with a counter of 2 to get the correct answer or the game ends
    if x == obstacleThreeX and y == obstacleThreeY:
        obstacleThree = True
        attemptsThree = 0
        print " "
        print "You have hit an obstacle! Answer the following question correctly to pass."
        print " "
        while obstacleThree == True:
            answerThree = str(raw_input("What was the room number class Programming Concepts COMI-1150-205 met in on Wednesdays at 6:00 PM?(numeric form): "))
            if answerThree == "2306":
                print " "
                print "Correct, you shall pass."
                print " "
                obstacleThree = False
            elif answerThree != "2306":
                print " "
                print "That was incorrect! You have one more attempt to get it correct or goodbye. "
                print " "
                attemptsThree = attemptsThree + 1
            if attemptsThree == 2:
                    obstacleThree = False
                    bMove = False
                    
    turns = turns + 1 #players turns added after all possible encounters have been reached
    if turns == 20:
        bMove = False
    if bMove == False: #end game (loser)
        print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
        print " "
        print "You have used all your turns or ran out of attempts. The game is over."
        print " "
    #helpful information for the user at the end of each turn    
    print "=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|="
    print " "
    print "Turns Used:" + str(turns)
    print " "
    print "===================="
    print " "
    print "Your current grid: " + str(x) + "," + str(y)
    print " "
    print "=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|="
    print " "
    #end game (winner)
    if x == treasureX and y == treasureY:
        bMove = False
        print "Congratulations! You found the treasure!"
        print " "
        print "The Game is now over."