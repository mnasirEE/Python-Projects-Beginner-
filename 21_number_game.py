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
    #
    if user_demand == "f":
        
    elif user_demand == "s":
        
    #
    else:
        print("Enter valid input: ")
        player_choice(total_cards, list_of_cards, current_player)

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