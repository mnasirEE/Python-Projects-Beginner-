import random 
computer_number = random.randint(0,100)
condition = True
while condition:
    user_guess = int(input("Enter a Number: "))
    if user_guess < computer_number:
        print("Enter a greater number: ")
    elif user_guess > computer_number:
        print("Enter a smaller number: ")
    elif user_guess == computer_number:
        print("You win") 
        condition = False


