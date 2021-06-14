from math import *

cmd1 = 0
cmd2 = 0
eq = 1
tm = 2

def ask():
    print("ζ(s)")
    print("")
    cmd1 = complex(input("s = "))
    cmd2 = int(input("Accuracy = "))
    print("")
    ans(eq,tm,cmd1,cmd2)

def ans(eq,tm,cmd1,cmd2):
    eq += 1/(tm**cmd1)
    tm+=1

    if tm >= cmd2:
        print("ζ(",cmd1,") = ",eq)
        print("________________________________")
        print("")
        ask()
    else:
        ans(eq,tm,cmd1,cmd2)

ask()
