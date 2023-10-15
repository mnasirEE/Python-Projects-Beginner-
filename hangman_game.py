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
    display_user_guess(secret_word, user_guess)
    print(destination_word)
    if destination_word == secret_word:
        print("Good Job\n You win")
        break
    else: 
        continue 

if destination_word != secret_word: 
    print("\nYour chances are finished")
    print("\nYou lose")    
    
 

