import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,4,5,6,7,8,9]
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
 