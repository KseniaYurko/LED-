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
def lightNumber(Number):
    decNumber == Number
    decToBinList(decNumber)
    for i in range (len(number)):
        if number[i] == '0':
            board.digital[N[i]].write(0)
        elif number[i] == '1':
            board.digital[N[i]].write(1)
Number = int(input('Введите число от 0 до 255: '))
lightNumber(Number)