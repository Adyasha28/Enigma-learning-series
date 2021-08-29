
player1_left=1
player1_right=1
player2_left=1
player2_right=1
print("Intial status")
print("Player1:", player1_left, player1_right)
print("Player2:", player2_left, player2_right)
count=1
while count>0:
    move1=input("enter A for attack and S for split for player1")
    if move1=='A':
        attack=input("LR or RL")
        if attack=='LR' :
            player2_right=player2_right+player1_left
            if player2_right>=5 :
                player2_right=0

        elif(attack=='RL'):
            player2_left=player2_left+player1_right
            if player2_left>=5:
                player2_left=0
        elif(attack=='LL'):
            player2_left=player2_left+player1_left
            if player2_left>=5:
                player2_left=0
        elif(attack=='RR'):
            player2_right=player2_right+player1_right
            if player2_right>=5:
                player2_right=0
        elif move1=='S':
            comb = input("Enter the combination")
            player1_left = comb[1]
            player1_right = comb[2]
    print("Player1:", player1_left, player1_right)
    print("Player2:", player2_left, player2_right)
    if (player2_left == 0 and player1_right == 0) or (player2_left == 0 and player2_right == 0):
        count = 0
        if player1_left == 0 and player1_right == 0:
            print("Player2 is winner")
            break
        else:
            print("Player1 is winner")
            break

    move2=input("enter A for attack and S for split for player2")    
    if move2=='A':
           attack=input("LR or RL")
           if attack=='LR' :
               player1_right=player1_right+player2_left
               if player1_right>=5 :
                   player1_right=0

           elif(attack=='RL'):
               player1_left=player1_left+player2_right
               if player1_left>=5:
                   player1_left=0
           elif(attack=='LL'):
               player1_left=player1_left+player2_left
               if player1_left>=5:
                   player1_left=0
           elif(attack=='RR'):
               player1_right=player1_right+player2_right
               if player1_right>=5:
                    player1_right=0  
    elif move2=='S':
        comb2 = input("Enter the combinaton: ")
        player2_left = comb2[1]
        player2_right = comb2[2]
    print("Player1:", player1_left, player1_right)
    print("Player2:", player2_left, player2_right)
    if (player1_left == 0 and player1_right == 0) or (player2_left == 0 and player2_right == 0):
        count = 0
        if player1_left == 0 and player1_right == 0:
            print("Player2 is winner")
        else:
            print("Player1 is winner")


print("Game Ends:P")



