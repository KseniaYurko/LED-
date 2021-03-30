import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,5,7,6,4,8,9]

def DARKall():
    for i in range (len(N)):
        board.digital[N[i]].write(0)
DARKall() 

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range (blinkCount):
        board.digital[N[ledNumber]].write(1)
        time.sleep(blinkPeriod)
        board.digital[N[ledNumber]].write(0)
        time.sleep(blinkPeriod)
ledNumber = int(input('Введи номер светодиода: '))
blinkCount = int(input('Количество миганий: '))
blinkPeriod = float(input('Интервал: '))
blink(ledNumber, blinkCount, blinkPeriod)