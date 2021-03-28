import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,4,5,6,7,8,9]

def lightUp(ledNumber, period):
    board.digital[N[ledNumber]].write(1)
    time.sleep(period)
    board.digital[N[ledNumber]].write(0)
ledNumber = int(input('Введи номер светодиода: '))
period = float(input('Время: '))
lightUp(ledNumber, period)
