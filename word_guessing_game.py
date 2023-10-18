# import random module for the selection of secret word
import random

# first user enters his name 
user_name = input("Enter your Name: ")

# Welcome message
print(f"\n{user_name}, Welcome to Nasir's Word Guessing Game")

# create a list of fruits
list_of_words = ["banana", "grapes", "mango"]
# selection of secret word from the list of words
secret_word = random.choice(list_of_words)
# length of secret_word
secret_word_length = len(secret_word)
# number of guesses 
chances = secret_word_length + 2

# printing chances
print("\nThe total chances you have: ",chances)

# making copy of secret word 
# that is basically used for letters that are present more than once in secret word
copy_of_secret_word = secret_word

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
    global copy_of_secret_word
    # if user guess is already present in destination word then do nothing
    if user_guess in destination_word:
        pass
    # otherwise check one by one letter that whether user_guess is present in destination_word or not
    else:
        # how many times a user guess or letter is present in secret word
        occurrence_in_secret_word = secret_word.count(user_guess)

        # it used to control the occurrence of elements which occurs more than once 
        occurrence_of_user_guess = 1

        # for loop to check the elements or letters of a secret word whether user guess 
        # is present in secret_word or not
        for index in range(len(secret_word)):

            # if user guess or user alphabet is present in secret word
            
            if user_guess.lower() == secret_word[index]:

                # if ocuurrence of letter is one
                if occurrence_in_secret_word == 1:
                        
                        # converting the destination word into a list to change its letters
                        destination_word_list = list(destination_word)
                        # changing _ with the user guess of destination word
                        destination_word_list[index] = user_guess.lower()
                        # converting the list back into string of destination word
                        destination_word = str("".join(destination_word_list))

                # if occurrence is more than 1
                elif occurrence_in_secret_word > 1:
                    # if letter is at its first place or ocurrence
                    if  occurrence_of_user_guess == 1:
                        # converting the destination word into a list to change its letters
                        destination_word_list = list(destination_word)
                        # changing _ with the user guess of destination word
                        destination_word_list[index] = user_guess.lower()
                        # converting the list back into string of destination word
                        destination_word = str("".join(destination_word_list))
                    else:  
                        # converting the destination word into a list to change its letters
                        destination_word_list = list(destination_word)
                        # changing _ with the user guess of destination word
                        destination_word_list[(occurrence_of_user_guess - 1) + next_index_user_guess] = user_guess.lower()
                        # converting the list back into string of destination word
                        destination_word = str("".join(destination_word_list))

                    # finding index of user_guess in copy of secret word
                    index_user_guess = copy_of_secret_word.find(user_guess) 
                    # finding value or letter at index_user_guess
                    copy_index_user_guess = copy_of_secret_word[index_user_guess]
                    # converting the copy of secret word into list of letters
                    list_copy_of_secret_word = list(copy_of_secret_word)
                    # remove the first occurence of user guess from copy of secret word
                    # while secret word remains safe
                    list_copy_of_secret_word.pop(index_user_guess)
                    # converting list of letters back into string of letters as copy of secret word
                    copy_of_secret_word = str("".join(list_copy_of_secret_word))
                    # next index of occurrence of user value
                    next_index_user_guess = copy_of_secret_word.find(user_guess)
                    # increasing the value of index of alphabet
                    occurrence_of_user_guess += 1
                # otherwise continue    
                else:
                    continue
                # if loop ends once then again make occurrence_of_user_guess 1
                occurrence_of_user_guess = 1
                

# game_loop
for index in range(chances):

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
        print("\n *** Good Job ***\n*** You win ***")
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
    print("\n*** Your chances are finished ***")
    print("\n*** You lose ***")    
    
 

