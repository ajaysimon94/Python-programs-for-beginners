while True:
    print("Enter your 1st value")
    userinput1 = int(input())
    print("Enter your 2nd value")
    userinput2 = int(input())
    print("Enter the operator + - / or *")
    userinput3 = input()

    if userinput3 == "+":
        print(userinput1+userinput2)
    elif userinput3 == "-":
        print(userinput1-userinput2)
    elif userinput3 == "*":
        print(userinput1*userinput2)
    elif userinput3 == "/":
        print(userinput1/userinput2)
    else:
        print("Incorrect value")
    answer = input("Would you like to continue - Y or N")
    if answer =="Y":
        continue
    else:
        print("Thank you")
        break
quit()