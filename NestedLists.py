numbers = [1, 2, 3, 4, 5, 6]
newNumbers = [[1, 2, 3], [4, 5, 6]]
index_1 = newNumbers[1]
number_6 = index_1[2]
number_2 = newNumbers[0][1]
print(newNumbers)
print(index_1)
print(number_6)
print(number_2)

print('---------------------------------')

for li in newNumbers:
    for num in li:
        print(num)

print('---------------------------------')

copyList = [[print(num) for num in li] for li in newNumbers]
# print(copyList)

print('---------------------------------')

generatedList = [num for num in range(1, 4)]
generatedNestedList = [
    ['X' if newNum % 2 == 0 else 'O' for newNum in range(1, 4)] for num in range(1, 4)]

print(generatedList)
print(generatedNestedList)
