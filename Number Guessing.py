import random

print("Welcome to the Number guessing game!!!")

secret_number = random.randint(1,100)
attempts = 10

while attempts > 0:
    guess = int(input("Guess the secret number between 1 and 100 : "))
    
    if secret_number > guess:
        print("Too Low, Try a higher number!")

    elif secret_number < guess:
        print("Too high, Try a lower number!")
    
    if secret_number == guess:
        print(f"Congratulations!! you guessed the correct number! The secret number was {secret_number}")
        break
    attempts -= 1
    print(f'Attempts left : {attempts}')

if attempts == 0:
    print(f"Oops! Game Over :( ..... The secret number was {secret_number})")