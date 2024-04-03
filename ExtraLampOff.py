n = int(input())

if n >= 1 and n <= 9:
    print('1')
elif n > 9 and n <= 99:
    print('2')
elif n > 99 and n <= 999:
    print('3')
elif n > 999 and n < 10000:
    print('4')
else:
    print('The input value must be between 1 and 10000.')
