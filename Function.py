# def Hello(name):
#     print('Hello, name')


# def Bay():
#     print('Good bay')


# def Sum(a, b):
#     result = a + b
#     return print(result)

def hoghoogh(hour, perHour):
    if hour > 0:
        result = hour * perHour
        return print(result)
    elif hour <= 0:
        print('hoghooghi daryaft nakardid.')
    else:
        print('Error!')


hour = input('Pleaase enter work hours: ')
perHour = input('Pleaase enter work per hours: ')
hour = int(hour)
perHour = int(perHour)

hoghoogh(hour, perHour)

# Hello('Yasin')
# Bay()

# num_1 = 2
# num_2 = 3

# Sum(num_1, num_2)
