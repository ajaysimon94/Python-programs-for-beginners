from pygame import mixer
from datetime import datetime
from time import time

def musicplay(File):
    mixer.init()
    mixer.music.load("bensound.mp3")
    mixer.music.play(-1)
    while True:
        a = input("enter s to stop the music\n")
        if a == "s":
            mixer.music.stop()
            break

init_water = time()
init_stand = time()
standgap =  7200 #every 2 hour
watergap =  3600 #every 1 hour

today = datetime.now()
today10AM = today.replace(hour=10, minute=0, second=0)
today6PM = today.replace(hour=18, minute=0, second=0)
print(f"The start time of program is {datetime.now()}")

if today > today10AM and today <today6PM:
    while True:
        if today > today10AM and today < today6PM:
            if time()-init_water >= watergap:
                musicplay("bensound.mp3")
                b = input(f"It's time to drink water: {datetime.now()}. Press c to confirm that you drank water\n")
                init_water = time()
                with open("logfile_water.txt","a+") as log:
                    log.write(f"Drank water at {datetime.now()}\n")
            if time()-init_stand >= standgap:
                musicplay("bensound.mp3")
                b = input(f"It's time to stand up: {datetime.now()}. Press c to confirm that you stood up\n")
                init_stand = time()
                with open("logfile_stand.txt","a+") as log:
                    log.write(f"Stood up at {datetime.now()}\n")
                continue
        else:
            quit()


quit()

