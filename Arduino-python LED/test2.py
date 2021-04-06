import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,5,7,6,4,8,9]

def DARKall():
    for i in range (len(N)):
        board.digital[N[i]].write(0)
DARKall()   
led = board.get_pin('6')
def lightUp(ledNumber, period):
    if ledNumber >3:
        board.analog_input[N[ledNumber]].write(1023)
        time.sleep(period)
        board.analog[N[ledNumber]].write(0)
    if ledNumber <3:
        board.digital[N[ledNumber]].write(1)
        time.sleep(period)
        board.digital[N[ledNumber]].write(0)
    else:
        print('ERROR!!! у тебя всего 8 светодиодов!!!')    
ledNumber = int(input('Введи номер светодиода: '))
period = float(input('Время: '))
lightUp(ledNumber, period)
