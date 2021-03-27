import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,4,5,6,7,8,9]

def runningDark(count, period):
    for i in range (8):
        board.digital[N[i]].write(1)
    for i in range(count):
        board.digital[N[ledNumber]].write(0)
        time.sleep(period)
        board.digital[N[ledNumber]].write(1)
        if N[ledNumber]<9:
            N[ledNumber]=N[ledNumber]+1
        elif N[ledNumber]>=9:
            N[ledNumber]=N[ledNumber]-7
ledNumber = int(input('С какого светодиода начинать? '))
count = int(input('Сколько раз переключить светодиод? '))
period = float(input('Интервал: '))
runningDark(count, period)