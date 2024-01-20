myNumbers = [1, 2, 3, 4, 5, 6]

print(myNumbers[0])
print(myNumbers[1])
print(myNumbers[2])
print(myNumbers[3])
print(myNumbers[4])
print(myNumbers[5])


myColors = ['red', 'blue', 'green', 3.5, 'yellow', 'orange']

for color in myColors:
    if type(color) == str:
        print(f"The color is: {color}")
    else:
        print(f"The number is: {color}")

print('----------------------')

index = 0
while index < len(myColors):
    color = myColors[index]

    if type(color) == str:
        print(f"The color is: {color}")
    else:
        print(f"The number is: {color}")

    index += 1
