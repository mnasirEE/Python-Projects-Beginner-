# import random module for the selection of secret word
import random
# create a list of fruits
list_of_words = ["mango", "grapes"]
# selection of secret word from the list of words
secret_word = random.choice(list_of_words)
# length of secret_word
secret_word_length = len(secret_word)
# number of guesses
chances = secret_word_length + 2

# creating a variable whose length is according to the secret word and 
# which is filled with dashes
destination_word = ""
for i in range(len(secret_word)):
    destination_word = destination_word + "_"
   

# function to print the word after each guess or turn of the user
# this function takes two arguments secret_word and user_guess

def display_user_guess(secret_word, user_guess):
    # we made destination_word, a global variable because
    # we want to change it into another function 
    global destination_word
    for i in range(len(secret_word)):
        if user_guess.lower() == secret_word[i]:
            
            destination_word_list = list(destination_word)
            destination_word_list[i] = user_guess.lower()
            destination_word = str("".join(destination_word_list))
            
        else:
            continue
                

# game_loop
for i in range(chances):

    # user guess an alphabet at a time 
    user_guess = input("\nEnter an alphabet: ")
    # calling a display function to display 
    # the secret word alphabets with dashes and replace
    # the dashes with user guess alphabet 
    # if user entered alphabet is present in the secret word 
    display_user_guess(secret_word, user_guess)
    # printing the output of above function
    print(destination_word)
    # checking that the user guessed word is same as secret word
    # if user guessed word is equal to secret word
    if destination_word == secret_word: 
        # if user guessed word is equal to secret word
        # print player wins
        print("Good Job\n You win")
        # if player or user wins, exit from loop, no need to use all chances
        break
    # otherwise user guessed word is not equal to secret word
    # continue to give chances to the user
    else:
        # next iteration of loop begins by this statement 
        continue 

# if all chances of user are finished, it means user guessed word is 
# not equal to secret word
# so, user lose the game
if destination_word != secret_word: 
    print("\nYour chances are finished")
    print("\nYou lose")    
    
 

