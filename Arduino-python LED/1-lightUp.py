import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,5,7,6,4,8,9]

def DARKall():
    for i in range (len(N)):
        board.digital[N[i]].write(0)
DARKall()   

def lightUp(ledNumber, period):
    board.digital[N[ledNumber]].write(1)
    time.sleep(period)
    board.digital[N[ledNumber]].write(0)
ledNumber = int(input('Введи номер светодиода: '))
period = float(input('Время: '))
lightUp(ledNumber, period)
