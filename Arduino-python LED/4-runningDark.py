import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,5,7,6,4,8,9]

def DARKall():
    for i in range (len(N)):
        board.digital[N[i]].write(0)
DARKall() 

def LIGHTall():
    for i in range (len(N)):
        board.digital[N[i]].write(1)   

def runningDark(count, period):
    ledNumber = int(input('С какого светодиода начинать? '))
    LIGHTall()
    while count>0:
        board.digital[N[ledNumber]].write(0)
        time.sleep(period)
        board.digital[N[ledNumber]].write(1)
        count = count-1
        ledNumber=ledNumber+1
        if ledNumber == 8:
            ledNumber = ledNumber-8
count = int(input('Сколько раз переключить светодиод? '))
period = float(input('Интервал: '))
runningDark(count, period)
DARKall() 
