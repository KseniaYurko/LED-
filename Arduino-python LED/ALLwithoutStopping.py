import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,4,5,6,7,8,9]

def closeAll(all):
    for i in range (len(N)):
        board.digital[N[i]].write(0)

def lightUp(ledNumber, period):
    board.digital[N[ledNumber]].write(1)
    time.sleep(period)
    board.digital[N[ledNumber]].write(0)
lightUp(1, 3)

def lightDown(lednumber,period):
    board.digital[N[ledNumber]].write(0)
    time.sleep(period)
    board.digital[N[ledNumber]].write(1)

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range (blinkCount):
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)
blink(6, 10, 0.5)
closeAll(all)

def runningLight(count, period):
    ledNumber = 0
    for i in range(count):
        lightUp(ledNumber, period)
        if N[ledNumber]<9:
            N[ledNumber]=N[ledNumber]+1
        elif N[ledNumber]>=9:
            N[ledNumber]=N[ledNumber]-7
closeAll(all)
runningLight(60, 0.1)

def runningDark(count, period):
    for i in range (8):
        board.digital[N[i]].write(1)
    for i in range(count):
        lightDown(ledNumber, period)
        if N[ledNumber]<9:
            N[ledNumber]=N[ledNumber]+1
        elif N[ledNumber]>=9:
            N[ledNumber]=N[ledNumber]-7
ledNumber = 0
runningDark(60, 0.1)
closeAll(all)


def decToBinList(decNumber):
    a = bin(decNumber)
    b = a[2::]
    number = list(b)
    c = len(number)
    for i in range (8-c):
        number.insert(i, '0')
    print(number)
decNumber = 244
decToBinList(decNumber)

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
    time.sleep(5)
decNumber = 244
lightNumber(decNumber)

def runningPattern(pattern, direction):
    a = bin(pattern)
    b = a[2::]
    number = list(b)
    c = len(number)
    for i in range (8-c):
        number.insert(i, '0')
    print(number)
    if direction == 1:
        for i in range(50):
            number.insert(0, number[7])
            number.pop(8)
            for i in range (8):
                if number[i] == '0':
                    board.digital[N[i]].write(0)
                elif number[i] == '1':
                    board.digital[N[i]].write(1)
            time.sleep(0.2)
    elif direction == 0:
        for i in range(50):
            number.insert(8, number[0])
            number.pop(0)
            for i in range (8):
                if number[i] == '0':
                    board.digital[N[i]].write(0)
                elif number[i] == '1':
                    board.digital[N[i]].write(1)
            time.sleep(0.2)
runningPattern(3, 0)
closeAll(all)