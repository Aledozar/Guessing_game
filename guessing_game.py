import random

def play_game():
    #generate random number betwwen 1 and 100
    secret_number = random.randint(1,100)

    attempts = 0
    max_attempts = 3

    print("Welcome to the number guessing game")
    print("Im thinking about a number between 1 and 100")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess"))
        except ValueError:
            print("Invalid input please enter a number")
            continue

        attempts +=1

        if guess < secret_number:
            print("Too low, try again")
        elif guess > secret_number:
            print("Too high, keep going")
        else: 
            print(F"Congratulations you guessed the number {secret_number} in {attempts} attempts")
            break
    else:
        print(F"Sorry you reached the maximum number of attemtps, the secret number was {secret_number}")

if __name__ == "__main__":
    play_game()