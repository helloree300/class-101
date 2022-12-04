import time

from playsound import playsound

def countdown_timer(seconds):
    while seconds>0:
        mins= int(seconds/60)
        sec= int(seconds%60)
        timer= f"{mins}:{sec}"
        print(timer)
        seconds-=1
    print("time up")
    playsound("mixkit-sound.wav")

s=int (input("enter the time and number of seconds: "))
countdown_timer(s)
