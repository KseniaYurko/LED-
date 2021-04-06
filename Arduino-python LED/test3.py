import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
 

led = board.get_pin('a:4:i')
pinA0 = board.get_pin('a:4:i')
pinA0.mode = pyfirmata.OUTPUT
pinA0.write(1)
time.sleep(3)
pinA0.write(4)
time.sleep(3)
