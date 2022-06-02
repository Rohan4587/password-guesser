# importing random
from random import *

# taking input from user
user_pass = input("Enter your password")

# storing alphabet letter to use thm to crack password
# password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
#             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
#             'w', 'x', 'y', 'z',]
password=['1', '2', '3', '4', '5', '6','7','6','8', '9','0']

# initializing an empty string
guess = ""


# using while loop to generate many passwords untill one of
# them does not matches user_pass
i=0
while (guess != user_pass):
    i=i+1
    guess = ""
    # generating random passwords using for loop
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0, 10)]
        guess = str(guess_letter) + str(guess)

    # printing guessed passwords
    print(guess)
    
# printing the matched password
print(f'trial {i}')
print(f"Your password {guess}")

input()