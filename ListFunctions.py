from cgi import print_arguments


myCourses = ['python', 'csharp', 'asp.net']
print(myCourses)

myCourses.append('django')
print(myCourses)

myCourses.extend(['java', 'jquery'])
print(myCourses)

# گسترش - آخر لیست
myCourses.extend(['java', 'jquery'])
print(myCourses)

myCourses.insert(0, 'php')
print(myCourses)

print('-----------------------------------')

myFriends = ['yasin', 'hasti', 'abbas', 'yasin', 'sobhan']

# myFriends.clear()

# myFriends.pop(1)

# myFriends.remove('hasti')

# print(myFriends.index('yasin'))

# print(myFriends.index('yasin', 1, 4))

# print(myFriends.count('yasin'))

# print(myFriends.reverse())

myFriends.sort()
print(myFriends)

friend = " - ".join(myFriends)
print(friend)
