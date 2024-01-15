name = input('Please enter your name: ')
number = input('Enter your number: ')
number = int(number)

# while number > 0:
#     print(number)
#     number -= 1

while number > 0:
    print(number)
    number += 1

    if number == 100:
        print('End.')
        print('--------')
        break

print('Sorry, ', name)
