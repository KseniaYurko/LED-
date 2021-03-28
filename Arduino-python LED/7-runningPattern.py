import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,4,5,6,7,8,9]

def closeAll(all):
    for i in range (8):
        board.digital[N[i]].write(0)
closeAll(all)


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
closeAll(all)

