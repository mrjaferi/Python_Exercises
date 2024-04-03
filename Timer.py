entryTime = input()
entryTime = int(entryTime)

hour = entryTime // 3600
entryTime = entryTime % 3600

minute = entryTime // 60

second = entryTime % 60

print(f'{hour} : {minute} : {second}')
