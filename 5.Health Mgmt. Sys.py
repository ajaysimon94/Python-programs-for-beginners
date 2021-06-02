import datetime

print("Welcome to J's health management system\n")

while True:
    def getdate():
        import datetime
        return datetime.datetime.now()

    def client(c):
        if c == "Harry" and fileinput == 1:
            with open("Harry-diet.txt","a+") as h1:
                h1file = input("Enter diet details\n")
                h1.write(str(getdate().ctime())+":"+h1file+"\n")
                print("record saved")
        elif c == "Harry" and fileinput == 2:
            with open("Harry-excercise.txt","a+") as h2:
                h2file = input("Enter exercise details\n")
                h2.write(str(getdate().ctime())+":"+h2file+"\n")
                print("record saved")
        if c == "Rohan" and fileinput == 1:
            with open("Rohan-diet.txt","a+") as r1:
                r1file = input("Enter diet details\n")
                r1.write(str(getdate().ctime())+":"+r1file+"\n")
                print("record saved")
        elif c == "Rohan" and fileinput == 2:
            with open("Rohan-excercise.txt","a+") as r2:
                r2file = input("Enter exercise details\n")
                r2.write(str(getdate().ctime())+":"+r2file+"\n")
                print("record saved")
        if c == "Hammad" and fileinput == 1:
            with open("Hammad-diet.txt","a+") as ham1:
                ham1file = input("Enter diet details\n")
                ham1.write(str(getdate().ctime())+":"+ham1file+"\n")
                print("record saved")
        elif c == "Hammad" and fileinput == 2:
            with open("Hammad-excercise.txt","a+") as ham2:
                ham2file = input("Enter exercise details\n")
                ham2.write(str(getdate().ctime())+":"+ham2file+"\n")
                print("record saved")

    def display(d):
        if d == "Harry" and displaytype == "1":
            with open("Harry-diet.txt") as h1:
                for i in h1:
                    print(i,end="")
        elif d == "Harry" and displaytype == "2":
            with open("Harry-excercise.txt") as h1:
                for i in h1:
                    print(i,end="")
        elif d == "Rohan" and displaytype == "1":
            with open("Rohan-diet.txt") as h1:
                for i in h1:
                    print(i,end="")
        elif d == "Rohan" and displaytype == "2":
            with open("Rohan-excercise.txt") as h1:
                for i in h1:
                    print(i,end="")
        elif d == "Hammad" and displaytype == "1":
            with open("Hammad-diet.txt") as h1:
                for i in h1:
                    print(i,end="")
        elif d == "Hammad" and displaytype == "2":
            with open("Hammad-excercise.txt") as h1:
                for i in h1:
                    print(i,end="")

    type = input("would you like to update date or view data? - Enter U or V\n")
    if type == "U":
        name = input("Which client data would you like to update?\nHarry, Rohan or Hammad\n")
        fileinput = int(input("Would you like to enter diet or excercise\nPress 1 for diet and 2 for excercise\n"))
        client(name)
    elif type == "V":
        displayclient = input("Which client date would you like to view? - Harry, Rohan or Hammad\n")
        displaytype = input("Press 1 for diet, 2 for excercise\n")
        display(displayclient)
    else:
        print("You seem to have incorrect data")

    cont = input("Would you like to continue? - Y or N\n")
    if cont == "Y":
        continue
    else:
        print("Thank you for using this system developed by Ajay")
        break
        quit()
