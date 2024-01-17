# GOD

def Even(a):
    if (a % 2) == 0:
        print(a)


primeNumber = 1
inputNumber = input('Enter your number: ')
inputNumber = int(inputNumber)

while primeNumber <= inputNumber:
    Even(primeNumber)

    primeNumber += 1
