import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,4,5,6,7,8,9]

def lightNumber(number):
    a = bin(decNumber)
    b = a[2::]
    print(b)
    number = list(b)
    c = len(number)
    for i in range (8-c):
        number.insert(i, '0')
    print(number)
    for i in range (len(number)):
        if number[i] == '0':
            board.digital[N[i]].write(0)
        elif number[i] == '1':
            board.digital[N[i]].write(1)
decNumber = int(input('Введите число от 0 до 255: '))
lightNumber(decNumber) 