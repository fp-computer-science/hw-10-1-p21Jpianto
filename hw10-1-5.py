# Author: JAp (amdg) 12/9/20

def cardbuster():
    x = int(input(" What is your first card? Please note that Jack, Kings and Queens are worth 10 pts. An ace = 11."))
    y = int(input(" What is your second card? Please note that Jack, Kings and Queens are worth 10 pts. An ace = 11"))
    if x + y > 21:
        print("You have busted :(")
    else:
        print("You are safe")


print(cardbuster())
