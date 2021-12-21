import random


Ladder = {}
Snake = {}

print()
print("Welcome to Snake And Ladder Game !!! ")
print()

class SnakeAndLadder :

    no_of_snake = int(input("How Many Snake You Want : "))

    for i in range(no_of_snake):
        snake_head = int(input("Head Value of Snake : "))
        snake_tail = int(input("Tail Value of Snake : "))
        Snake.update({snake_head:snake_tail})
        print()

    print(f"Snakes are : {Snake}")
    print()

    no_of_ladder = int(input("How Many Ladder You Want : "))

    for i in range(no_of_ladder):
        ladder_start = int(input("Start Value of Ladder : "))
        ladder_end = int(input("End Value of Ladder : "))
        Ladder.update({ladder_start:ladder_end})
        print()

    print(f"Ladders are : {Ladder}")
    print()

    def Snake_Bite():   
        for x,y in Snake.items():
            if position == x:
                position = y

    def Climb_Ladder():
        for x,y in Ladder.items():
            if position == x:
                position = y

    def PlayerName():
        Player1_Name = None
        while not Player1_Name:
            Player1_Name = input("Please Enter a Name For Player 1 : ").strip()

        Player2_Name = None
        while not Player2_Name:
            Player2_Name = input("Please Enter a Name For Player 2 : ").strip()

        print()
        print("Match will be played between : ",Player1_Name ,"And " ,Player2_Name)
        return Player1_Name,Player2_Name

    PlayerName()

    Player1_Position = 0
    Player2_Position = 0

    Recent1_Position = Player1_Position
    Recent2_Position = Player2_Position


    def Move(position):
        dice = random.randint(1,6)
        print(f"Dice:{dice}")
        position = position + dice
        if position > 100:
            position = position - dice
        if position <= 100:
            if position in Snake :
                print("Bitten by Snake")
                position = Snake[position]
                print(f"Position:{position}")
    
            elif position in Ladder :
                print("Climbed by Ladder")
                position = Ladder[position]
                print(f"Position:{position}")

            else :
                print(f"Position:{position}")
    
        print()
        return position

    while True :
        A = input("Player 1 Enter \"A\" to throw dice : ")
        Recent1_Position = Move(Recent1_Position)
        if Recent1_Position == 100:
            print("Game Over !!! \n Player 1 Won. !!! ")
            break

        B = input("Player 2 Enter \"B\" to throw dice : ")
        Recent2_Position = Move(Recent2_Position)
        if Recent2_Position == 100:
            print("Game Over !!! \n Player 1 Won. !!! ")
            break
