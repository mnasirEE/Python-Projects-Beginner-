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
# game_loop
for i in range(chances):

    # user guess an alphabet at a time 
    user_guess = input("Enter an alphabet: ")
    
 

