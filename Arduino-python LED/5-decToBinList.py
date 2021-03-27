import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,4,5,6,7,8,9]

def decToBinList(decNumber):
    b = bin(decNumber)
    b1 = b[2::]
    print(b1)
    number = list(b1)
    a = len(number)
    for i in range (8-a):
        number.insert(i, '0')
    print(number)
    for i in range (len(number)):
        if number[i] == '0':
            board.digital[N[i]].write(0)
        elif number[i] == '1':
            board.digital[N[i]].write(1)
decNumber = int(input('Введите число от 0 до 255: '))
decToBinList(decNumber) 