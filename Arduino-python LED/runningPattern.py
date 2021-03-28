import pyfirmata
import time

board = pyfirmata.Arduino("COM4")
N = [2,3,4,5,6,7,8,9]

def runningPattern(pattern, direction):
    b = bin(pattern)
    b1 = b[2::]
    print(b1)
    number = list(b1)
    a = len(number)
    for i in range (8-a):
        number.insert(i, '0')
    print(number)
    
    if direction == 'right':
        a == 0
        for a in range(count):
            for i in range (len(number)): #высветил число
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
direction = str(input('В какую сторону?'))
runningPattern(pattern, direction)