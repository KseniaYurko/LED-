import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,4,5,6,7,8,9]
for i in range (len(N)):
    board.digital[N[i]].write(1)