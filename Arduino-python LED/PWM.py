import pyfirmata
from time import sleep

board = pyfirmata.Arduino("COM4")



board.digital[3].write(0)

try:
    board.digital[3].ChangeDutyCycle(50)
    input('F=50Hz, DC=50%. Press Enter...')
    board.digital[3].ChangeDutyCycle(20)
    input('F=50Hz, DC=20%. Press Enter...')
    board.digital[3].ChangeFrequency(10)
    board.digital[3].ChangeDutyCycle(80)
    input('F=10Hz, DC=80%. Press Enter...')
    board.digital[3].ChangeDutyCycle(10)
    input('F=10Hz, DC=10%. Press Enter to exit...')
except KeyboardInterrupt:
    pass

pwm.stop()
