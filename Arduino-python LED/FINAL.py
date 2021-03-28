import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,4,5,6,7,8,9]

print ('ЗДАДАНИЕ №1 - lightUp')
def lightUp(ledNumber, period):
    board.digital[N[ledNumber]].write(1)
    time.sleep(period)
    board.digital[N[ledNumber]].write(0)
ledNumber = int(input('Введи номер светодиода: '))
period = float(input('Время: '))
lightUp(ledNumber, period)
print()


print ('ЗДАДАНИЕ №1* - lightDown - для №5')
def lightDown(lednumber,period):
    board.digital[N[ledNumber]].write(0)
    time.sleep(period)
    board.digital[N[ledNumber]].write(1)
ledNumber = int(input('Введи номер светодиода: '))
period = float(input('Время: '))
lightDown(ledNumber, period)
print()


print ('ЗДАДАНИЕ №2 - blink')
def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range (blinkCount):
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)
ledNumber = int(input('Введи номер светодиода: '))
blinkCount = int(input('Количество миганий: '))
blinkPeriod = float(input('Интервал: '))
blink(ledNumber, blinkCount, blinkPeriod)
print()


print ('ЗДАДАНИЕ №3 - runningLight')
def runningLight(count, period):
    for i in range(count):
        lightUp(ledNumber, period)
        if N[ledNumber]<9:
            N[ledNumber]=N[ledNumber]+1
        elif N[ledNumber]>=9:
            N[ledNumber]=N[ledNumber]-7
ledNumber = int(input('С какого светодиода начинать? '))
count = int(input('Сколько раз переключить светодиод? '))
period = float(input('Интервал: '))
runningLight(count, period)
print()


print ('ЗДАДАНИЕ №4 - runningDark')
def runningDark(count, period):
    for i in range (8):
        board.digital[N[i]].write(1)
    for i in range(count):
        lightDown(ledNumber, period)
        if N[ledNumber]<9:
            N[ledNumber]=N[ledNumber]+1
        elif N[ledNumber]>=9:
            N[ledNumber]=N[ledNumber]-7
ledNumber = int(input('С какого светодиода начинать? '))
count = int(input('Сколько раз переключить светодиод? '))
period = float(input('Интервал: '))
runningDark(count, period)
print()


print ('ЗДАДАНИЕ №5 - decToBinList')
def decToBinList(decNumber):
    a = bin(decNumber)
    b = a[2::]
    number = list(b)
    c = len(number)
    for i in range (8-c):
        number.insert(i, '0')
    print(number)
decNumber = int(input('Введите число от 0 до 255: '))
decToBinList(decNumber)
print()


print ('ЗДАДАНИЕ №6 - lightNumber')
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
print()


print ('ЗДАДАНИЕ №7 - runningPattern')
def runningPattern(pattern, direction):
    decToBinList(pattern)
    if direction == 'right':
        for i in range(count):
            for i in range (len(number)):
                if number[i] == '0':
                    board.digital[N[i]].write(0)
                elif number[i] == '1':
                    board.digital[N[i]].write(1)
    elif direction == 'left':
        for i in range(count):    
            for i in range (len(number)):
                if number[i] == '0':
                    board.digital[N[i]].write(0)
                elif number[i] == '1':
                    board.digital[N[i]].write(1) 
          
pattern = int(input('Введите число от 0 до 255: '))
count = int(input('Сколько раз передвинуть? '))
direction = str(input('В какую сторону? '))
runningPattern(pattern, direction)
