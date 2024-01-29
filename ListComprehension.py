from ast import Num


myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# doubleNumbers = []
# for num in myNumbers:
#     doubleNumbers.append(num * 2)

doubleNumbers = [num * 2 for num in myNumbers]
print(myNumbers)
print(doubleNumbers)

myName = 'yasin'
namesCharacters = [char.upper() for char in myName]
print(namesCharacters)

print('----------------------------------------------')

even = [num for num in myNumbers if num % 2 == 0]
odd = [num for num in myNumbers if num % 2 != 0]
print(even)
print(odd)

newList=[num *2 if num % 2 == 0 else num * 3 for num in myNumbers]
print(newList)