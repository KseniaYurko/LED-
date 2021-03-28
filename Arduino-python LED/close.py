import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,4,5,6,7,8,9]

def closeAll(all):
    for i in range (8):
        board.digital[N[i]].write(0)
closeAll(all)
