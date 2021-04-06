import pyfirmata
from pyfirmata import Arduino, INPUT, PWM
import time

board = pyfirmata.Arduino("COM4")

it = pyfirmata.util.Iterator(board)
it.start()

LED = board.get_pin('d:5:p')

l = 0
count = int(input('Сколько раз повторить? '))
for i in range(count):
    while l<=1:
        LED.write(l)
        time.sleep(0.01)
        LED.write(0)
        l = l + 0.01
    while l>=0:
        LED.write(l)
        time.sleep(0.01)
        LED.write(0)
        l = l - 0.01        