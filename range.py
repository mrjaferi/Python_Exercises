from unittest import result


# myNumbers = range(1,21)
# result=list(myNumbers)
# print(result)
print(list(range(1, 10)))

# print(list(range(0, 10)))
print(list(range(10)))

print(list(range(1, 15, 2)))
print(list(range(0, 15, 2)))

print(list(range(10, 1, -1)))
print(list(range(10, 1, -2)))

print('-----------------------------')

for num in range(1, 10):
    print('*' * num)


print('-----------------------------')

for num in range(1,10):
    if num % 2 == 1:
        for star in range(1,6):
            print('*' * star)
    else:
        for star in range(6,0,-1):
            print('*' * star)