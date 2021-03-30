import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,5,7,6,4,8,9]

def DARKall():
    for i in range (len(N)):
        board.digital[N[i]].write(0)
DARKall() 

def runningLight(count, period):
    ledNumber = int(input('С какого светодиода начинать? '))
    while count>0:
        board.digital[N[ledNumber]].write(1)
        time.sleep(period)
        board.digital[N[ledNumber]].write(0)
        count = count-1
        ledNumber=ledNumber+1
        if ledNumber == 8:
            ledNumber = ledNumber-8
count = int(input('Сколько раз переключить светодиод? '))
period = float(input('Интервал: '))
runningLight(count, period)

DARKall() 