nTile = 5
mTile = 4

n, m = input().split(" ")
n = int(n) * 100
m = int(m) * 100

a = (n * m)

aTile = nTile * mTile

numberTiles = a // aTile
print(numberTiles)
