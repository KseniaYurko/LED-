import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,4,5,6,7,8,9]

def runningLight(count, period):
    for i in range(count):
        board.digital[N[0]].write(1)
        time.sleep(period)
        board.digital[N[0]].write(0)
        if N[0]<9:
            N[0]=N[0]+1
        elif N[0]>=9:
            N[0]=N[0]-7
runningLight(600, 0.1)