import random
print("Number guessing game")
#We are going to use a function called randint to generate numbers randomly
number = random.randint(1,9)
chances = 0
print("Guess a number between 1-9: ")
while chances < 5:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print(" Congratulations, you won!")
        break
    elif guess < number:
        print("Your guess was lower than the actual number, guess again: ", guess)
    else: 
        print("Your guess was too high, guess a number lower: ", guess)
    chances = chances + 1
if not chances < 5:
    print("You lose. The number is: ", number)