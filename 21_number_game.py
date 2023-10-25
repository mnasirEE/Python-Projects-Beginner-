# importing random module
import random
# total number of cards
total_cards = 21
# first creating cards list
list_of_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                  13, 14, 15, 16, 17, 18, 19, 20, 21]
# current player
current_player = 1

# play game loop
def player_choice(total_cards, list_of_cards, current_player):
    # user wants to play first or second or want his first turn or second 
    user_demand = input("Enter 'f' for first and enter 's' for second\nWant to play first or second: ") 
    while len(list_of_cards) != 0:
        if user_demand == "f":
            # player turn
            if len(list_of_cards) !=0:
                number_of_cards = int(input("How many cards you want to pick: "))
                for choice in range(number_of_cards):
                    print("You can pick cards from this list\n",list_of_cards)
                    print("choose your cards")
                    pick_cards = int(input(">> "))
                    list_of_cards.remove(pick_cards)
            if len(list_of_cards) !=0:
                # current_player = current_player    
                # computer turn
                # 2nd player
                current_player = 3 - current_player
                computer_num_of_cards = random.randint(1,3)
                computer_num_of_cards = random.randint(1,3)
                if len(list_of_cards) == 2 or len(list_of_cards) > 2:
                    for comp_choice in range(computer_num_of_cards):
                        computer_pick_cards = random.choice(list_of_cards)

                        list_of_cards.remove(computer_pick_cards)
                else:
                    computer_pick_cards = random.choice(list_of_cards)

                    list_of_cards.remove(computer_pick_cards)
             
            # total_cards = total_cards - number_of_cards - computer_num_of_cards
            
               


        
        elif user_demand == "s":
            if len(list_of_cards)!=0:
                # computer turn
                # 1st player
                
                current_player = 1
                computer_num_of_cards = random.randint(1,3)
                if len(list_of_cards) == 2 or len(list_of_cards) > 2:
                    for comp_choice in range(computer_num_of_cards):
                        computer_pick_cards = random.choice(list_of_cards)

                        list_of_cards.remove(computer_pick_cards)
                    
                else:
                    computer_pick_cards = random.choice(list_of_cards)

                    list_of_cards.remove(computer_pick_cards) 
                

            if len(list_of_cards) !=0:
                # player turn
                # second player
                current_player = 3 - current_player
                number_of_cards = int(input("How many cards you want to pick: "))
                for choice in range(number_of_cards):
                    print("You can pick cards from this list\n",list_of_cards)
                    print("choose your cards")
                    pick_cards = int(input(">> "))
                    list_of_cards.remove(pick_cards) 
                

            # total_cards = total_cards - number_of_cards - computer_num_of_cards 
        #
        else:
            print("Enter valid input: ")
            

# Game loop
def game_loop():
    # printing " Enter 'y' for yes and enter 'n' for no: " to tell the user what to do
    print("Enter 'y' for yes and enter 'n' for no: ")
    # taking input from user
    user_choice = input("Do you want to play:")
    # if user choice is yes then
    if user_choice.lower() == "y":
        # play game
        player_choice(total_cards, list_of_cards, current_player)
    # if user choice is no exit the game 
    elif user_choice.lower() == "n":
        # exit from game loop
        exit()  
    # if neither yes nor no, then tell user enter valid input    
    else:
        # printing Enter valid input
        print("Enter valid input: ")
        # again start game loop
        game_loop() 
# starting the game loop first time             
game_loop()

# winner
print(f"player{current_player} has last card")
print(f"So, the winner is player{3-current_player}")