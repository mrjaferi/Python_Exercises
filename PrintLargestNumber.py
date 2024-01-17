# GOD

number_1 = input('Please enter number 1: ')
number_2 = input('Please enter number 2: ')
number_3 = input('Please enter number 3: ')
number_1 = int(number_1)
number_2 = int(number_2)
number_3 = int(number_3)

if number_3 > number_1 and number_3 > number_2:
    print(number_3)
elif number_2 > number_1 and number_2 > number_3:
    print(number_2)
elif number_1 > number_2 and number_1 > number_3:
    print(number_1)
else:
    print('Error: Input error!')
