import random

def play(x, y):
    computer_choice = random.randint(1, highestRange)
    for attempt in range(1, tries+1):
        guess = int(input(f"[{attempt}/{tries}] Guess (1-{highestRange}): "))
        
        if guess > computer_choice:
            print("Too high!")

        elif guess < computer_choice:
            print("Too low!")

        else:
            print(f"Correct! You got it in {attempt} tries")
            best_attempt = 8
            if best_attempt > attempt:
                best_attempt = attempt
            
            else:
                best_attempt = best_attempt

            print(f"Best score this session: {best_attempt} tries")
            play_again = input("Play again? (y/n)")

            if play_again == "y":
                break

            elif play_again == "n":
                exit()

    print(f"The number was {computer_choice}")
    

play_again = "y"
tries = 7
while play_again == "y":
    difficulty_level = int(input("Enter difficulty level(1,2 or 3):"))
    
    if difficulty_level == 1:
        highestRange = 100 
        print("Easy Level") 
        play(highestRange, tries)

    elif difficulty_level == 2:
        highestRange = 300
        print("Medium Level")
        play(highestRange, tries)

    elif difficulty_level == 3:
        highestRange = 500
        print("High Level")
        play(highestRange, tries)