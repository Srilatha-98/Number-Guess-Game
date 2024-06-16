#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I've selected a number between 1 and 10. Try to guess it!")

    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try guessing higher.")
        elif guess > secret_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
            break

        if attempts == 5:
            print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}. Better luck next time!")
            break

# Run the game
guessing_game()


# In[ ]:




