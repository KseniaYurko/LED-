import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,5,7,6,4,8,9]

def DARKall():
    for i in range (len(N)):
        board.digital[N[i]].write(0)
DARKall()        

def LIGHTall():
    for i in range (len(N)):
        board.digital[N[i]].write(1)

print ('ЗДАДАНИЕ №1 - lightUp')
print ('Свечение заданной лампочки заданное время.')
def lightUp(ledNumber, period):
    board.digital[N[ledNumber]].write(1)
    time.sleep(period)
    board.digital[N[ledNumber]].write(0)
ledNumber = int(input('Введи номер светодиода: '))
period = float(input('Время: '))
lightUp(ledNumber, period)
print()


print ('ЗДАДАНИЕ №2 - blink')
print ('Мигание заданной лампочки заданное кол-во раз.')
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
print()


print ('ЗДАДАНИЕ №3 - runningLight')
print ('"Бегущий огонек" с заданного номера светодиода')
def runningLight(count, period):
    ledNumber = int(input('С какого светодиода начинать? '))
    while count>0:
        board.digital[N[ledNumber]].write(1)
        time.sleep(period)
        board.digital[N[ledNumber]].write(0)
        count = count-1
        ledNumber=ledNumber+1
        if ledNumber == 8:
            ledNumber = ledNumber-8
count = int(input('Сколько раз переключить светодиод? '))
period = float(input('Интервал: '))
runningLight(count, period)
print()


print ('ЗДАДАНИЕ №4 - runningDark')
print ('"Бегущий огонек" с заданного номера светодиода')
def runningDark(count, period):
    ledNumber = int(input('С какого светодиода начинать? '))
    LIGHTall()
    while count>0:
        board.digital[N[ledNumber]].write(0)
        time.sleep(period)
        board.digital[N[ledNumber]].write(1)
        count = count-1
        ledNumber=ledNumber+1
        if ledNumber == 8:
            ledNumber = ledNumber-8
count = int(input('Сколько раз переключить светодиод? '))
period = float(input('Интервал: '))
runningDark(count, period)
DARKall()
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
for i in range (8):
    board.digital[N[i]].write(0)
decNumber = int(input('Введите число от 0 до 255: '))
decToBinList(decNumber)
print()



print ('ЗДАДАНИЕ №6 - lightNumber')
print ('Светящееся бинарное число')
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
DARKall()
print()

print ('ЗДАДАНИЕ №7 - runningPattern')
print ('"Бегущий узор" заданное число раз')
def runningPattern(pattern, direction):
    a = bin(pattern)
    b = a[2::]
    number = list(b)
    c = len(number)
    for i in range (8-c):
        number.insert(i, '0')
    print(number)
    if direction == 1:
        for i in range(count):
            number.insert(0, number[7])
            number.pop(8)
            for i in range (8):
                if number[i] == '0':
                    board.digital[N[i]].write(0)
                elif number[i] == '1':
                    board.digital[N[i]].write(1)
            time.sleep(period)
    elif direction == 0:
        for i in range(count):
            number.insert(8, number[0])
            number.pop(0)
            for i in range (8):
                if number[i] == '0':
                    board.digital[N[i]].write(0)
                elif number[i] == '1':
                    board.digital[N[i]].write(1)
            time.sleep(period)

pattern = int(input('Введите число от 0 до 255: '))
count = int(input('Сколько раз передвинуть? '))
period = float(input('Интервал: '))
direction = int(input('В какую сторону? (1-вправо; 0-влево) '))
runningPattern(pattern, direction)
DARKall()