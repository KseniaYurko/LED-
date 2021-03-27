import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,4,5,6,7,8,9]

def runningDark(count, period):
    for i in range (8):
        board.digital[N[i]].write(1)
    for i in range(count):
        board.digital[N[0]].write(0)
        time.sleep(period)
        board.digital[N[0]].write(1)
        if N[0]<9:
            N[0]=N[0]+1
        elif N[0]>=9:
            N[0]=N[0]-7
runningDark(300, 0.2)