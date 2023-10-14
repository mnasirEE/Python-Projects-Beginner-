# import random module for the selection of secret word
import random
# create a list of fruits
list_of_words = ["banana", "mango", "grapes", "greyfruit"]
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

# game_loop
for i in range(chances):

    # user guess an alphabet at a time 
    user_guess = input("Enter an alphabet: ")
    
 

