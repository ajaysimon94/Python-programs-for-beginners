while True:
    n=int(input("Enter a number\n"))
    bool=int(input("Enter 1 or 0"))
    c=n

    if bool == 1:
        while True:
            if c==0:
                break
            elif c <= n:
                print(str(n) * c)
                c = c - 1
                continue

    elif bool == 0:
        c = 1
        while True:
            if c <= n:
                print(str(n) * c)
                c = c+1
                continue
            elif c>n:
                break
    cont = input("Would you like to continue> Y or N\n")
    if cont == "Y":
        continue
    else:
        quit()


