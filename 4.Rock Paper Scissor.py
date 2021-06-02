import random

print("Welcome to Rock Paper Scissor game\n")

print("Developed by Ajay")
play = ["Rock","Paper","Scissor"]
print("Game instructions:\n")
print("There will be 10 play-offs","Winner will be decided basis all 10 play-offs")

while True:
    player_score = 0
    computer_score = 0
    attempt = 0
    while True:
        while attempt < 10:
            x = input("Please enter your input:\n")
            y = random.choice(play)
            if x == "Rock" and y == "Paper":
                print(y)
                print("Computer wins")
                computer_score = computer_score+1
                print("Your score is: ",player_score)
                print("Computer score is: ",computer_score)
                attempt = attempt+1
                continue
            elif x == "Rock" and y == "Rock":
                print(y)
                print("It's a tie. You both get one point each")
                player_score = player_score+1
                computer_score = computer_score+1
                print("Your score is: ", player_score)
                print("Computer score is: ", computer_score)
                attempt = attempt + 1
                continue
            elif x == "Rock" and y == "Scissor":
                print(y)
                print("You win")
                player_score = player_score+1
                print("Your score is: ", player_score)
                print("Computer score is: ", computer_score)
                attempt = attempt + 1
                continue
            elif x == "Paper" and y == "Paper":
                print(y)
                print("It's a tie. You both get one point each")
                player_score = player_score+1
                computer_score = computer_score+1
                print("Your score is: ", player_score)
                print("Computer score is: ", computer_score)
                attempt = attempt + 1
                continue
            elif x == "Paper" and y == "Rock":
                print(y)
                print("You win")
                player_score = player_score+1
                print("Your score is: ", player_score)
                print("Computer score is: ", computer_score)
                attempt = attempt + 1
                continue
            elif x == "Paper" and y == "Scissor":
                print(y)
                print("Computer wins")
                computer_score = computer_score+1
                print("Your score is: ", player_score)
                print("Computer score is: ", computer_score)
                attempt = attempt + 1
                continue
            elif x == "Scissor" and y == "Paper":
                print(y)
                print("You win")
                player_score = player_score+1
                print("Your score is: ", player_score)
                print("Computer score is: ", computer_score)
                attempt = attempt + 1
                continue
            elif x == "Scissor" and y == "Rock":
                print(y)
                print("Computer wins")
                computer_score = computer_score+1
                print("Your score is: ", player_score)
                print("Computer score is: ", computer_score)
                attempt = attempt + 1
                continue
            elif x == "Scissor" and y == "Scissor":
                print(y)
                print("It's a tie. You both win one point each")
                computer_score = computer_score+1
                player_score = player_score+1
                print("Your score is: ", player_score)
                print("Computer score is: ", computer_score)
                attempt = attempt + 1
                continue
            else:
                print("You have entered invalid input")
                cont_input = input("Would you like to play again? Y or N\n")
                if cont_input == "Y":
                    player_score = 0
                    computer_score = 0
                    attempt = 0
                    continue
                else:
                    print("Thank you for playing")
                    quit()
        print("The final scores are :-\n")
        print("Computer:",computer_score)
        print("You:", player_score)
        if computer_score == player_score:
            print("It's a tie")
        elif player_score > computer_score:
            print("*****Congrats. You won!!*****")
        else:
            print("Oops. Better luck next time, the computer won")
        cont_input = input("Would you like to play again? Y or N\n")
        if cont_input == "Y":
            player_score = 0
            computer_score = 0
            attempt = 0
            continue
        else:
            print("Thank you for playing")
            quit()

    quit()