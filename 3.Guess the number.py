import random

attempt = 1
print("Welcome to 'Guess the number game'.\n You get 9 attempts to guess the correct number!")
print("Developed by Ajay")
print("")

while int(attempt)<10:
    try:
        if attempt == 1:
            guess = random.randint(0, 100)
        print("Enter your guess number")
        userinput = int(input())
        #print(guess)
        if attempt == 9 and userinput != guess:
            print("Game over. The guess number was:",guess)
        elif userinput == guess:
            print("Congrats you have guessed the right number in attempt number:",attempt)
            print("Would you like to play again? - Y or N")
            playinput = input()
            if playinput == "Y":
                attempt = 1
                continue
            elif playinput == "N":
                print("Okay, Thank you")
                quit()
        elif userinput > guess:
            print("Your number is higher than the 'guess number'. You only have",9-attempt,"attempts left")
            print("")
            attempt = attempt + 1
            continue
        elif userinput < guess:
            print("Your number is lesser than the 'guess number'.You only have",9-attempt,"attempts left")
            print("")
            attempt = attempt + 1
            continue

        print("Would you like to play again? - Y or N")
        playinput = input()
        if playinput == "Y":
            attempt = 1
            continue
        else:
            quit()
    except Exception as e:
        print("Oops, looks like you entered an invalid character. The game only accepts numbers")
        print("Would you like to play again? - Y or N")
        playinput = input()
        if playinput == "Y":
            attempt = 1
            continue
        else:
            break
            quit()