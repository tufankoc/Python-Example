import random
number = random.randint(1, 100)
claim = 20

while claim > 0:
    guess = int(input("Guess the number: "))
    if guess < 0:
        print("You can't guess a negative number!")
        continue
    elif guess == number:
        print("You guessed it!" + " Final score: " + str(20 - claim))
        break
    elif guess < number:
        print("Too low!") # guess < number
    else:
        print("Too high!") # guess > number
    claim -= 1
    if claim == 0:
        print("You lost!") 
        print("The number was", number) 
        break   
    print("You have", claim, "guesses left.")   # print the number of guesses left
print("Game over!")
